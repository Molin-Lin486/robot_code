import cv2
import numpy as np
import time

cap = cv2.VideoCapture(0)

print("操作指南：")
print("n: 正常彩色 | y: 灰度图 | t: 二值化")  # 把 gray 改成 y，单字母好按
print("b: 蓝色通道 | g: 绿色通道 | r: 红色通道")
print("s: 拍照保存 | q: 退出")

mode = 'normal'

while True:
    ret, frame = cap.read()
    if not ret: break

    # --- 核心逻辑：通道分离 ---
    # OpenCV 默认顺序是 B, G, R (蓝，绿，红)
    b_channel, g_channel, r_channel = cv2.split(frame)

    if mode == 'normal':
        display_frame = frame
    elif mode == 'gray':
        display_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    elif mode == 'threshold':
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        _, display_frame = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    
    # 这里的显示逻辑：如果你选了 b，就显示拆分出来的蓝色矩阵
    elif mode == 'b': display_frame = b_channel
    elif mode == 'g': display_frame = g_channel
    elif mode == 'r': display_frame = r_channel

    cv2.imshow('Robot Vision', display_frame)

    key = cv2.waitKey(1) & 0xFF
    
    # 按键判断 - 全部改成单字母，修复 bug
    if key == ord('n'): mode = 'normal'      # n = normal（正常）
    if key == ord('y'): mode = 'gray'       # y = 灰度的拼音首字母，原来 gray 是4个字母会出错！
    if key == ord('t'): mode = 'threshold'  # t = threshold（二值化/阈值）
    if key == ord('b'): mode = 'b'           # b = blue（蓝色通道）
    if key == ord('g'): mode = 'g'           # g = green（绿色通道）
    if key == ord('r'): mode = 'r'           # r = red（红色通道）
    if key == ord('s'):                      # s = save（保存）
        if key == ord('s'):
            name = f"face_{int(time.time())}.jpg" # 用时间戳做名字，保证不重复
            cv2.imwrite(name, display_frame)
            print(f"已保存为 {name}")
        
    if key == ord('q'): break                # q = quit（退出）

cap.release()
cv2.destroyAllWindows()