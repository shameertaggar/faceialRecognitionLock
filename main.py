import cv2
import face_recognition
import subprocess
import time


print("storing faces")
# Load your own face images for training
image1 = face_recognition.load_image_file('/Users/shameerali/Desktop/q.jpg')
image2 = face_recognition.load_image_file('/Users/shameerali/Desktop/w.jpg')
# Add more images as needed

# Encode the face images
encoding1 = face_recognition.face_encodings(image1)[0]
encoding2 = face_recognition.face_encodings(image2)[0]
# Add more encodings as needed

# Create a list of known face encodings and their corresponding names
known_face_encodings = [encoding1, encoding2]
known_face_names = ['Shameer', 'Shameer']
# Make sure the face encodings and names are in the same order

# Load the pre-trained face cascade
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Initialize the video capture object
video_capture = cv2.VideoCapture(1)  # Change the index to the appropriate camera source (e.g., 0 for built-in webcam)

# Set the flag to indicate if the laptop is locked
is_locked = False

# Set the timer variables
timer_started = False
last_shameer_detection_time = time.time()
lock_threshold = 5  # Lock the laptop if no Shameer face detected for 5 seconds

# Delay in milliseconds (adjust as needed)
delay = 100

while True:
    # Wait for the specified delay
    cv2.waitKey(delay)
    print("frame detected")
    # Capture frame after the delay
    ret, frame = video_capture.read()

    if ret:
        # Convert the frame to grayscale for face detection
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect faces in the grayscale frame
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        # Reset the timer if a Shameer face is detected
        if len(faces) > 0:
            timer_started = True
            last_shameer_detection_time = time.time()

        # Check if the timer has exceeded the threshold
        if timer_started and (time.time() - last_shameer_detection_time) >= lock_threshold:
            is_locked = True

        # Iterate over the detected faces
        for (x, y, w, h) in faces:
            # Extract the face region from the frame
            face_image = frame[y:y+h, x:x+w]

            # Convert the face image to RGB for face recognition
            rgb_face = cv2.cvtColor(face_image, cv2.COLOR_BGR2RGB)

            # Encode the face image if a face is detected
            face_encodings = face_recognition.face_encodings(rgb_face)

            if len(face_encodings) > 0:
                face_encoding = face_encodings[0]

                # Compare the face encoding with the known face encodings
                matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
                name = "Unknown"

                if True in matches:
                    matched_index = matches.index(True)
                    name = known_face_names[matched_index]

                # Draw a rectangle around the face and display the name
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
                cv2.putText(frame, name, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0), 2)

                # Lock the laptop if the recognized face does not belong to you
                if name != 'Shameer' and not is_locked:
                    print("Locking laptop - Unknown face detected")
                    is_locked = True
                    subprocess.call(["osascript", "-e", 'tell application "System Events" to keystroke "q" using {control down, command down}'])

        # Display the resulting frame
        cv2.imshow('Video', frame)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# Release the video capture object and close the windows
video_capture.release()
cv2.destroyAllWindows()
