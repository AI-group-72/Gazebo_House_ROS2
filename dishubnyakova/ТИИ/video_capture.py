import cv2

# Захват видео с камеры
cap = cv2.VideoCapture(0)

# Или загрузка видео из файла
# cap = cv2.VideoCapture('path/to/video.mp4')

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    # Отображение кадра
    cv2.imshow('frame', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

