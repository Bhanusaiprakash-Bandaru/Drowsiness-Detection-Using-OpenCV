import cv2
import dlib
import pygame
from scipy.spatial import distance
from imutils import face_utils

pygame.mixer.init()
pygame.mixer.music.load("alert.wav")

def eye_aspect_ratio(eye):
    A = distance.euclidean(eye[1], eye[5])
    B = distance.euclidean(eye[2], eye[4])
    C = distance.euclidean(eye[0], eye[3])
    ear = (A + B) / (2.0 * C)
    return ear

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

(lStart, lEnd) = face_utils.FACIAL_LANDMARKS_IDXS["left_eye"]
(rStart, rEnd) = face_utils.FACIAL_LANDMARKS_IDXS["right_eye"]

cap = cv2.VideoCapture(0)
EYE_AR_THRESH = 0.25
EYE_AR_CONSEC_FRAMES = 20
counter = 0
ALARM_ON = False

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    rects = detector(gray, 0)

    for rect in rects:
        shape = predictor(gray, rect)
        shape = face_utils.shape_to_np(shape)

        leftEye = shape[lStart:lEnd]
        rightEye = shape[rStart:rEnd]
        leftEAR = eye_aspect_ratio(leftEye)
        rightEAR = eye_aspect_ratio(rightEye)
        ear = (leftEAR + rightEAR) / 2.0

        leftHull = cv2.convexHull(leftEye)
        rightHull = cv2.convexHull(rightEye)
        cv2.drawContours(frame, [leftHull], -1, (0, 255, 0), 1)
        cv2.drawContours(frame, [rightHull], -1, (0, 255, 0), 1)

        if ear < EYE_AR_THRESH:
            counter += 1
            if counter >= EYE_AR_CONSEC_FRAMES:
                if not ALARM_ON:
                    ALARM_ON = True
                    pygame.mixer.music.play()
                cv2.putText(frame, "DROWSINESS ALERT!", (100, 100),
                            cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 255), 3)
        else:
            counter = 0
            ALARM_ON = False
            pygame.mixer.music.stop()

        cv2.putText(frame, f"EAR: {ear:.2f}", (500, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

    cv2.imshow("Drowsiness Detection", frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
