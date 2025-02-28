
import cv2
import mediapipe as mp
import numpy as np

mp_pose = mp.solutions.pose
mp_draw = mp.solutions.drawing_utils

# Используйте абсолютный путь к видеофайлу
cap = cv2.VideoCapture('/Users/dusya/env/video-boo/video.mp4')

if not cap.isOpened():
    print("Ошибка: Не удалось открыть видеофайл.")
else:
    with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            
            # Создание копии кадра для отображения суставов
            frame_with_joints = frame.copy()
            
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = pose.process(rgb_frame)
            
            if results.pose_landmarks:
                mp_draw.draw_landmarks(frame_with_joints, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)
            
            # Объединение кадров в одно окно
            h, w, _ = frame.shape
            combined_frame = np.zeros((h, w*2, 3), dtype=np.uint8)
            combined_frame[:, :w] = frame
            combined_frame[:, w:] = frame_with_joints
            
            # Отображение объединенного кадра
            cv2.imshow('Combined', combined_frame)
            
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    cap.release()
    cv2.destroyAllWindows()
