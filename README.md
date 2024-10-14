# Face Detection Web Application

## Description

This project is a web application built with Flask that incorporates real-time face detection using OpenCV. The application allows users to access their webcam, detect faces in live video feeds, and display age and gender placeholders. Users can also download the recorded video of the session.

### Features

- **Real-time Face Detection**: Utilizes OpenCV to detect faces in a webcam feed.
- **Age and Gender Placeholders**: Displays placeholder text for age and gender on detected faces.
- **Video Recording**: Records the video feed and saves it as an AVI file.
- **Download Option**: Provides an option to download the recorded video.

### API Key

This application requires an OpenAI API key for certain functionalities. You will need to create a `api.env` file in the project root and add your API key as follows:
## Directory Structure
face-detection/                                 
  app.py                          
  api.env                   
  templates/                            
      index.html
Running the Application
To start the application, follow these steps:

Activate the Virtual Environment:
If you haven't already activated your virtual environment, do so by running:
bash
## Running the Application
#activated your virtual environment
Execute the following command in your terminal:
**python app.py**
Access the Application:
**Open your web browser and go 
http://localhost:5000**

 
