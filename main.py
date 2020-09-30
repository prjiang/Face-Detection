import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml') 

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
while True:
    ret, frame = cap.read()
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        print(faces)
        print('偵測到{0}人臉！'.format(len(faces)))
    
    cv2.namedWindow('img', cv2.WINDOW_NORMAL)
    cv2.imshow('img', frame)
    
    if cv2.waitKey(1)== ord('s'):
        cv2.imwrite('save.png', frame)
    if cv2.waitKey(1)== ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
