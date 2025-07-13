import cv2
import mediapipe as mp
import time
import math
import winsound
import threading

# Initialize mediapipe
mp_hands = mp.solutions.hands
mp_face = mp.solutions.face_mesh
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7, min_tracking_confidence=0.7)
face_mesh = mp_face.FaceMesh(max_num_faces=1)

# Initialize video capture
cap = cv2.VideoCapture(1)

# Thresholds
DISTANCE_THRESHOLD = 0.05  # Distance between mouth and hand (normalized)
ALERT_COOLDOWN = 3  # seconds between alerts
last_alert_time = 0


def play_alert():
    winsound.Beep(1000, 500)


def get_distance(p1, p2):
    return math.hypot(p2[0] - p1[0], p2[1] - p1[1])


while cap.isOpened():
    success, frame = cap.read()
    if not success:
        break

    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    hand_results = hands.process(rgb)
    face_results = face_mesh.process(rgb)

    hand_landmarks = None
    mouth_center = None

    # Get mouth center (face landmark 13 = upper lip, 14 = lower lip)
    if face_results.multi_face_landmarks:
        for face_landmarks in face_results.multi_face_landmarks:
            upper_lip = face_landmarks.landmark[13]
            lower_lip = face_landmarks.landmark[14]
            mouth_center = ((upper_lip.x + lower_lip.x) / 2, (upper_lip.y + lower_lip.y) / 2)

    # Draw face landmarks (optional)
    if mouth_center:
        h, w, _ = frame.shape
        cx, cy = int(mouth_center[0] * w), int(mouth_center[1] * h)
        cv2.circle(frame, (cx, cy), 5, (0, 255, 255), -1)

    # Detect hand and compare distance
    if hand_results.multi_hand_landmarks and mouth_center:
        h, w, _ = frame.shape
        for handLms in hand_results.multi_hand_landmarks:
            for tip_id in [4, 8, 12, 16, 20]:  # All 5 fingertips
                fingertip = handLms.landmark[tip_id]
                finger_pos = (fingertip.x, fingertip.y)
                distance = get_distance(finger_pos, mouth_center)

                # Draw circle at fingertip
                fx, fy = int(fingertip.x * w), int(fingertip.y * h)
                cv2.circle(frame, (fx, fy), 6, (255, 0, 0), -1)

                if distance < DISTANCE_THRESHOLD:
                    cv2.putText(frame, "Stop Biting!", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 255), 3)
                    if time.time() - last_alert_time > ALERT_COOLDOWN:
                        play_alert()
                        last_alert_time = time.time()
                    break  # Alert only once per frame


    cv2.imshow('Nail Biting Detector', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
