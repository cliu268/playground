import cv2

# load pre-trained data on face frontals from opencv
trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# To capture video from webcam 0 from default video source, or you can pass in video file
webcam = cv2.VideoCapture(0) #"D:\Pictures\Taiwan 2013\Video\P1020977.MP4")

# Iterate forever over frames
while True:

    # Read the current frame
    successful_frame_read, frame = webcam.read()

    # Must convert to grayscale
    grayscaled_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces
    face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)

    # Draw rectangles around the faces
    for (x, y, w, h) in face_coordinates:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Display the image with the faces spotted
    cv2.imshow('Face Detector', frame)
    key = cv2.waitKey(1)

    ### Stop if q or Q key is pressed
    if key==81 or key==113:
        break
## Release the VideoCapture object
webcam.release()

print("Code Complete")