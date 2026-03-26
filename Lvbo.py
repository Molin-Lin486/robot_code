import cv2

cap = cv2.VideoCapture(0)

print("T2 滤波实验指南：")
print("n: 正常 | 1: 均值滤波 | 2: 高斯滤波 | 3: 中值滤波 | 4: 二值化+中值(去噪演示)")
print("q: 退出")

mode = 'normal'

while True:
    ret, frame = cap.read()
    if not ret: break

    if mode == 'normal':
        display_frame = frame
    elif mode == '1':
        # 均值滤波：3x3 的九宫格
        display_frame = cv2.blur(frame, (3, 3))
    elif mode == '2':
        # 高斯滤波：最常用的磨皮
        display_frame = cv2.GaussianBlur(frame, (5, 5), 0)
    elif mode == '3':
        # 中值滤波：去胡椒粉噪声
        display_frame = cv2.medianBlur(frame, 5)
    elif mode == '4':
        # 进阶：先变黑白，再中值滤波（你会发现画面变得极其干净）
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        _, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
        display_frame = cv2.medianBlur(thresh, 5)

    cv2.imshow('T2 Filter Experiment', display_frame)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('n'): mode = 'normal'
    if key in [ord('1'), ord('2'), ord('3'), ord('4')]:
        mode = chr(key)
    if key == ord('q'): break

cap.release()
cv2.destroyAllWindows()