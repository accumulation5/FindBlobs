import sensor, image, time
#摄像头操作
sensor.reset()                      # Reset and initialize the sensor.
sensor.set_pixformat(sensor.RGB565) # RGB565 (or GRAYSCALE)
sensor.set_framesize(sensor.QVGA)   # Set frame size to QVGA (320x240)
#sensor.set_framesize(sensor.VGA)     # 高分辨率  640x480
#sensor.set_windowing((320, 160))     #窗口大小 取中间的320*160区域
sensor.skip_frames(time = 2000)     # Wait for settings take effect.

sensor.set_auto_gain(False)         #自动增益  True or False
sensor.set_auto_exposure(True)      #自动曝光  True or False
sensor.set_auto_whitebal(False)     #白平衡    True or False

#sensor.set_hmirror(True)            #水平方向翻转
#sensor.set_vflip(True)              #垂直方向翻转

clock = time.clock()                # Create a clock object to track the FPS.

#变量定义
ROI=(30,30,180,180)                 #ROI 感兴趣区域 x,y,w,h
#Blackcup=((5, 44, -53, -6, -24, 8))                       #black(0,0,0) blue(0,0,255) green(0,255,0) Red G Blue
RedBall=(39, 0, 22, 127, -128, 127)
Red=(255,0,0)
White=(255,255,255)

while(True):
    clock.tick()                    # Update the FPS clock.
    img = sensor.snapshot()         # Take a picture and return the image.
    #print(clock.fps())             # 打印 返回每秒帧数(FPS)

    statistics=img.get_statistics(roi=ROI)
    color_l_max=statistics.l_max()  #返回LAB 最值、平均数(mean)、众数(mode)等
    color_a_min=statistics.a_min()
    #print(color_l_max,color_a_min)
    #img.draw_line((100,20,100,180),color=(Red))  #画直线 x0,y0,x1,y1
    img.draw_rectangle(ROI)         #画框 默认白色
    black_blobs=img.find_blobs([RedBall],roi=ROI,x_stride=5,y_stride=5,area_threshold=20,pixels_threshold=50,merge=True)
    #x_stride:查找的色块的x方向上最小宽度的像素 area_threshold(面积阈值) pixels_threshold(像素个数阈值) merge:如果设置为True，那么合并所有重叠的blob为一个
    for blob in black_blobs:        #For循环画框 对blobs色块列表中每个blob色块画框
        if blob.area()>=100:
            img.draw_rectangle((blob.rect()),color=White)   #blob.rect() 返回这个色块的外框
            img.draw_cross(blob.cx(),blob.cy(),color=White) #画十字
            print("中心坐标：" + str(blob.cx()))       #blob.cx() 返回色块的外框的中心x坐标（int）






