import cv2  # import = 导入，cv2 = OpenCV 库的代码名字（计算机视觉库）

cap = cv2.VideoCapture(0)  # cap = 变量名（capture 缩写，捕捉），= = 赋值，cv2 = OpenCV，. = 的，VideoCapture = 视频捕捉类，(0) = 第0号摄像头（电脑自带）

while True:  # while = 当...时（循环），True = 真（永远成立），: = 冒号（循环开始）
   ret, frame = cap.read()  # ret = 变量名（return 返回值，是否成功），, = 逗号（多变量赋值），frame = 变量名（帧，单张画面），= = 赋值，cap = 摄像头对象，. = 点号（的），read() = 读取函数（抓一帧），() = 执行
   if not ret: break  # if = 如果，not = 非/不（取反），ret = 返回值，: = 冒号，break = 跳出循环（读取失败就退出）

   # --- 1. ROI 提取 (截取中间 200x200 的区域) ---  # # = 注释符号，--- = 装饰线，1. = 步骤1，ROI = Region of Interest（感兴趣区域），提取 = extract，截取 = cut，中间 = center，200x200 = 200像素宽×200像素高，区域 = area，() = 括号里中文解释
   h, w = frame.shape[:2]  # h = 变量名（height 缩写，高度），w = 变量名（width 缩写，宽度），, = 逗号（多变量赋值），= = 赋值，frame = 原图，. = 的，shape = 形状属性（返回高、宽、通道数），[:2] = 切片（取前两个值，就是高和宽，不要通道数），: = 冒号（切片符号），2 = 取到第2个（不包括第2个）
   cy, cx = h//2, w//2  # cy = 变量名（center y，中心点y坐标），cx = 变量名（center x，中心点x坐标），, = 逗号，= = 赋值，h//2 = 高度整除2（// = 整除符号，去掉小数），w//2 = 宽度整除2，, = 逗号分隔两个计算
   roi = frame[cy-100:cy+100, cx-100:cx+100]  # roi = 变量名（Region of Interest，感兴趣区域），= = 赋值，frame[...] = 从frame中切片取一部分，[cy-100:cy+100, = 第一个维度（y轴/高度方向）：从中心往上100到往下100，cx-100:cx+100] = 第二个维度（x轴/宽度方向）：从中心往左100到往右100，cy-100 = 中心y减100（上边界），cy+100 = 中心y加100（下边界），cx-100 = 中心x减100（左边界），cx+100 = 中心x加100（右边界），: = 切片符号（从...到...），, = 逗号分隔两个维度，整体就是切出200×200的正方形（中心点上下左右各100）

   # --- 2. 图像处理 (变成灰度) ---  # # = 注释，2. = 步骤2，图像处理 = image processing，变成 = become，灰度 = grayscale
   roi_gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)  # roi_gray = 变量名（ROI的灰度图），= = 赋值，cv2 = OpenCV，. = 的，cvtColor = convert color（转换颜色），(roi, = 第一个参数（ROI区域），cv2.COLOR_BGR2GRAY) = 第二个参数（从BGR彩色转灰度），COLOR = 颜色，BGR2GRAY = BGR to Gray
   # 把它变回 3 通道，否则无法和彩色原图融合  # # = 注释，把它 = take it，变回 = convert back，3通道 = 3 channels（BGR），否则 = otherwise，无法 = cannot，融合 = merge/blend
   roi_color = cv2.cvtColor(roi_gray, cv2.COLOR_GRAY2BGR)  # roi_color = 变量名（转回彩色的ROI），= = 赋值，cv2.cvtColor = 转换颜色，(roi_gray, = 灰度图，cv2.COLOR_GRAY2BGR) = 从灰度转回BGR，GRAY2BGR = Gray to BGR（灰度转彩色，虽然看起来是灰的，但有3个通道）

   # --- 3. 缩放 (Resize: 把 ROI 缩小一倍) ---  # # = 注释，3. = 步骤3，缩放 = resize/scale，Resize = 调整大小，把 = take，缩小 = shrink，一倍 = half size
   roi_small = cv2.resize(roi_color, (0,0), fx=0.5, fy=0.5)  # roi_small = 变量名（缩小后的ROI），= = 赋值，cv2.resize = OpenCV调整大小函数，(roi_color, = 第一个参数（要缩放的图），(0,0), = 第二个参数（输出大小，填0表示不指定，用fx/fy），fx=0.5, = 第三个参数（x方向缩放因子，0.5 = 一半），fy=0.5) = 第四个参数（y方向缩放因子，0.5 = 一半），f = factor（因子），x/y = 横/纵向，0.5 = 50%，即缩小一半

   # --- 4. 图像覆盖 (把缩小后的 ROI 贴到原图左上角) ---  # # = 注释，4. = 步骤4，图像覆盖 = image overlay/paste，把 = take，缩小后的 = resized，贴到 = paste to，左上角 = top-left corner
   # 算出缩小后的大小  # # = 注释，算出 = calculate，缩小后的 = after resizing，大小 = size
   sh, sw = roi_small.shape[:2]  # sh = 变量名（small height，缩小后的高度），sw = 变量名（small width，缩小后的宽度），, = 逗号，= = 赋值，roi_small = 缩小后的图，. = 的，shape = 形状，[:2] = 切片取前两个（高和宽）
   frame[0:sh, 0:sw] = roi_small  # frame[0:sh, 0:sw] = 原图的切片（左上角区域：y从0到sh，x从0到sw），= = 赋值（覆盖），roi_small = 缩小后的ROI，0:sh = 从0到缩小后的高度，0:sw = 从0到缩小后的宽度，就是把缩小图贴到原图左上角

   # --- 5. 数值计算 (给画面中心画个框，增强仪式感) ---  # # = 注释，5. = 步骤5，数值计算 = numerical calculation（这里指坐标计算），给 = give，画面 = frame，中心 = center，画个框 = draw a rectangle，增强 = enhance，仪式感 = sense of ceremony（视觉效果）
   cv2.rectangle(frame, (cx-100, cy-100), (cx+100, cy+100), (0, 255, 0), 2)  # cv2.rectangle = OpenCV画矩形函数，(frame, = 第一个参数（在哪张图画），(cx-100, cy-100), = 第二个参数（左上角坐标，元组），cx-100 = 中心x减100，cy-100 = 中心y减100，, = 逗号分隔坐标，(cx+100, cy+100), = 第三个参数（右下角坐标，元组），cx+100 = 中心x加100，cy+100 = 中心y加100，, = 逗号，(0, 255, 0), = 第四个参数（颜色，BGR格式，0蓝255绿0红 = 纯绿色），0 = 蓝色分量，255 = 绿色分量（最大），0 = 红色分量，2) = 第五个参数（线宽，2像素），rectangle = 矩形

   cv2.imshow('T2 Final Challenge: ROI & Transform', frame)  # cv2 = OpenCV，. = 的，imshow = image show（图像显示），('T2 Final Challenge: ROI & Transform', = 窗口标题字符串，T2 = 任务编号，Final Challenge = 最终挑战，ROI & Transform = 区域提取与变换），frame) = 要显示的图像（已经被修改过的）

   if cv2.waitKey(1) & 0xFF == ord('q'):  # if = 如果，cv2.waitKey = 等待按键，(1) = 等待1毫秒，& = 按位与，0xFF = 十六进制255（过滤高位），== = 等于判断，ord('q') = 字符q的ASCII码（113），: = 冒号
       break  # break = 跳出循环（退出程序）

cap.release()  # cap = 摄像头对象，. = 的，release = 释放（关闭摄像头硬件），() = 执行

cv2.destroyAllWindows()  # cv2 = OpenCV，. = 的，destroy = 销毁，All = 所有，Windows = 窗口，() = 关掉所有OpenCV窗口