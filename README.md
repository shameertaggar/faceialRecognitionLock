# Face Recognition and Laptop Locking System

This project utilizes face recognition to detect faces in a live video stream and lock the laptop if an unrecognized face is detected. The face recognition is based on pre-stored face images and encodings. This system can be used as a security measure to prevent unauthorized access to a laptop.

## Requirements
- Python 3.x
- OpenCV (`pip install opencv-python`)
- face_recognition (`pip install face_recognition`)

## Usage
1. Store face images for training in the project directory.
2. Adjust the `known_face_encodings` and `known_face_names` lists with the appropriate face encodings and corresponding names.
3. Ensure that the pre-trained face cascade file (`haarcascade_frontalface_default.xml`) is available in the OpenCV data directory.
4. Run the script and provide the appropriate camera source index (`video_capture = cv2.VideoCapture(1)`).

## Functionality
- The system continuously captures frames from the specified camera source.
- It uses the Haar Cascade classifier for face detection in the grayscale frame.
- If a face is detected, it starts a timer and resets it with each detection of a known face.
- If the timer exceeds a specified threshold, the laptop is considered locked.
- Face recognition is applied to known faces, and the recognized face's name is displayed on the frame.
- If an unrecognized face is detected, the laptop is locked.

## Keyboard Shortcut
- The laptop can be locked manually by pressing 'q'.

## Note
- This system serves as a demonstration and may require adjustments based on specific use cases.
- Ensure that the necessary libraries are installed before running the script.
