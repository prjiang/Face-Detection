import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml') # 載入分類器
# 從視訊鏡頭擷取影片
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
while True:
    # read the frame
    _, img = cap.read()
    
    # 轉灰階
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # 偵測臉部
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    # 繪製人臉部分方框
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
        print(faces)
        print('偵測到{0}人臉！'.format(len(faces)))
    
    # 視窗顯示
    cv2.namedWindow('img', cv2.WINDOW_NORMAL)
    cv2.imshow('img', img)
    
    # 儲存及退出
    if cv2.waitKey(30)== ord('s'):
        cv2.imwrite('save.png', img)
    if cv2.waitKey(30)== ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
