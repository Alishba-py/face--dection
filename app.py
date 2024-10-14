from flask import Flask, render_template, Response, send_file
import cv2
import os
from dotenv import load_dotenv
import openai

app = Flask(__name__)

# Load environment variables from the .env file
load_dotenv('api.env')  # Adjust the path as necessary
openai.api_key = os.getenv('OPENAI_API_KEY')

# Initialize the webcam
camera = cv2.VideoCapture(0)  # Use 0 for the default camera
is_streaming = True  # Flag to control video streaming
video_filename = 'output.avi'  # Output video file

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter(video_filename, fourcc, 20.0, (640, 480))

@app.route('/')
def index():
    return render_template('index.html')

def generate_frames():
    global is_streaming, out
    while is_streaming:
        success, frame = camera.read()
        if not success:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

        # Draw rectangles and add placeholders for age and gender
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
            age = "Age: 25"  # Replace with actual age detection logic
            gender = "Gender: Male"  # Replace with actual gender detection logic
            cv2.putText(frame, f"{age}, {gender}", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

        # Write the frame to the video file
        out.write(frame)

        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/stop_video')
def stop_video():
    global is_streaming, out
    is_streaming = False  # Set the flag to False to stop the video stream
    camera.release()  # Release the camera resource
    out.release()  # Release the video writer
    return "Video stopped"

@app.route('/download_video')
def download_video():
    return send_file(video_filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)