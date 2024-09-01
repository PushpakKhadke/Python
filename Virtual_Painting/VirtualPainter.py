import cv211
import numpy as np
import time
import os
import HandTrackingModule as htm
def virtual_Painter():
    # print("started")
    brushThickness = 5
    eraserThickness = 150
    folderPath = "Header"
    myList = os.listdir(folderPath)
    # print(myList)
    overlayList = []
    for imPath in myList:
        image = cv2.imread(f'{folderPath}/{imPath}')
        overlayList.append(image)
    # print(len(overlayList))
    header = overlayList[0]
    drawColor = (0, 0, 255)
    shape = 'freestyle'
    cap = cv2.VideoCapture(0)
    cap.set(3, 1280)
    cap.set(4, 720)
    detector = htm.handDetector(detectionCon=0, maxHands=1)
    xp, yp = 0, 0
    imgCanvas = np.zeros((720, 1280, 3), np.uint8)
    while True:

        # 1. Import image
        success, img = cap.read()
        img = cv2.flip(img, 1)

        # 2. Find Hand Landmarks
        img = detector.findHands(img)
        lmList = detector.findPosition(img, draw=False)

        if len(lmList) != 0:
            # print(lmList)

            # tip of index and middle fingers
            x1, y1 = lmList[8][1:]
            x2, y2 = lmList[12][1:]
            x0, y0 = lmList[4][1:]
            # 3. Check which fingers are up
            fingers = detector.fingersUp()
            # print(fingers)

            # 4. If Selection Mode - Two finger are up
            if fingers[1] and fingers[2]:
                xp, yp = 0, 0
                # print("Selection Mode")
                # # Checking for the click
                if y1 < 70:
                    if 15 < x1 < 60:
                        header = overlayList[0]
                        drawColor = (0, 0, 255)
                        shape = 'freestyle'
                    elif 75 < x1 < 120:
                        header = overlayList[16]
                        drawColor = (255, 1, 1)
                        shape = 'freestyle'
                    elif 130 < x1 < 180:
                        header = overlayList[20]
                        drawColor = (0, 255, 255)
                        shape = 'freestyle'
                    elif 195 < x1 < 240:
                        header = overlayList[4]
                        drawColor = (0, 255, 0)
                        shape = 'freestyle'
                    elif 255 < x1 < 300:
                        header = overlayList[8]
                        drawColor = (0, 150, 255)
                    elif 1184 < x1 < 1280:
                        header = overlayList[13]
                        drawColor = (0, 0, 0)
                        shape = 'freestyle'

                    #Tools
                    elif 663 < x1 < 753 and drawColor == (0, 0, 255):
                        header = overlayList[0]
                        shape = 'freestyle'
                    elif 789 < x1 < 879 and drawColor == (0, 0, 255):
                        header = overlayList[11]
                        shape = 'circle'
                    elif 919 < x1 < 1009 and drawColor == (0, 0, 255):
                        header = overlayList[14]
                        shape = 'rectangle'
                    elif 1052 < x1 < 1142 and drawColor == (0, 0, 255):
                        header = overlayList[15]
                        shape = 'ellipse'

                    elif 663 < x1 < 753 and drawColor == (255, 1, 1):
                        header = overlayList[16]
                        shape = 'freestyle'
                    elif 789 < x1 < 879 and drawColor == (255, 1, 1):
                        header = overlayList[17]
                        shape = 'circle'
                    elif 919 < x1 < 1009 and drawColor == (255, 1, 1):
                        header = overlayList[18]
                        shape = 'rectangle'
                    elif 1052 < x1 < 1142 and drawColor == (255, 1, 1):
                        header = overlayList[19]
                        shape = 'ellipse'

                    elif 663 < x1 < 753 and drawColor == (0, 255, 255):
                        header = overlayList[20]
                        shape = 'freestyle'
                    elif 789 < x1 < 879 and drawColor == (0, 255, 255):
                        header = overlayList[1]
                        shape = 'circle'
                    elif 919 < x1 < 1009 and drawColor == (0, 255, 255):
                        header = overlayList[2]
                        shape = 'rectangle'
                    elif 1052 < x1 < 1142 and drawColor == (0, 255, 255):
                        header = overlayList[3]
                        shape = 'ellipse'

                    elif 663 < x1 < 753 and drawColor == (0, 255, 0):
                        header = overlayList[4]
                        shape = 'freestyle'
                    elif 789 < x1 < 879 and drawColor == (0, 255, 0):
                        header = overlayList[5]
                        shape = 'circle'
                    elif 919 < x1 < 1009 and drawColor == (0, 255, 0):
                        header = overlayList[6]
                        shape = 'rectangle'
                    elif 1052 < x1 < 1142 and drawColor == (0, 255, 0):
                        header = overlayList[7]
                        shape = 'ellipse'

                    elif 663 < x1 < 753 and drawColor == (0, 150, 255):
                        header = overlayList[8]
                        shape = 'freestyle'
                    elif 789 < x1 < 879 and drawColor == (0, 150, 255):
                        header = overlayList[9]
                        shape = 'circle'
                    elif 919 < x1 < 1009 and drawColor == (0, 150, 255):
                        header = overlayList[10]
                        shape = 'rectangle'
                    elif 1052 < x1 < 1142 and drawColor == (0, 150, 255):
                        header = overlayList[12]
                        shape = 'ellipse'


                cv2.rectangle(img, (x1, y1 - 25), (x2, y2 + 25), drawColor, cv2.FILLED)
            if fingers[1] and fingers[2] == False:
                cv2.circle(img, (x1, y1), 15, drawColor)
                # print("Drawing Mode")
                if xp == 0 and yp == 0:
                    xp, yp = x1, y1

                cv2.line(img, (xp, yp), (x1, y1), drawColor, brushThickness)


                if drawColor == (0, 0, 0):
                    eraserThickness = 50
                    z1, z2 = lmList[4][1:]
                    # print(z1,z2)
                    result = int(((((z1 - x1) ** 2) + ((z2 - y1) ** 2)) ** 0.5))
                    # print(result)
                    if result < 0:
                        result = -1 * result
                    u = result
                    if fingers[1] and fingers[4]:
                        eraserThickness = u
                    # print(eraserThickness)
                    cv2.putText(img, str("eraserThickness="), (0, 700), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)
                    cv2.putText(img, str(int(eraserThickness)), (450, 700), cv2.FONT_HERSHEY_PLAIN, 3,
                                (255, 0, 255), 3)
                    cv2.line(img, (xp, yp), (x1, y1), drawColor, eraserThickness)
                    cv2.line(imgCanvas, (xp, yp), (x1, y1), drawColor, eraserThickness)

                else:
                    brushThickness = 5
                    # z1, z2 = lmList[4][1:]
                    # print(z1,z2)
                    # result = int(((((z1 - x1) ** 2) + ((z2 - y1) ** 2)) ** 0.5))
                    # print(result)
                    # if result < 0:
                    #     result = -1 * result
                    # u = result
                    # brushThickness = int(u)
                    # print(eraserThickness)

                    # draw
                    if shape == 'freestyle':
                        z1, z2 = lmList[4][1:]
                        # print(z1,z2)
                        result = int(((((z1 - x1) ** 2) + ((z2 - y1) ** 2)) ** 0.5))
                        # print(result)
                        if result < 0:
                            result = -1 * result
                        u = result
                        cv2.line(img, (xp, yp), (x1, y1), drawColor, brushThickness)
                        if u<=25:
                            cv2.line(imgCanvas, (xp, yp), (x1, y1), drawColor, brushThickness)
                            cv2.line(img, (xp, yp), (x1, y1), drawColor, brushThickness)
                        cv2.putText(img, str(u), (600, 700), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)
                        cv2.putText(img, str("brushThickness="), (0, 700), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)
                        cv2.putText(img, str(int(brushThickness)), (450, 700), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255),3)
                        cv2.line(imgCanvas, (xp, yp), (x1, y1), drawColor, brushThickness)

                    # Rectangle
                    if shape == 'rectangle':
                        z1, z2 = lmList[4][1:]
                        # print(z1,z2)
                        result = int(((((z1 - x1) ** 2) + ((z2 - y1) ** 2)) ** 0.5))
                        # print(result)
                        if result < 0:
                            result = -1 * result
                        u = result
                        cv2.rectangle(img, (x0, y0), (x1, y1), drawColor)
                        cv2.putText(img, "Length of Diagonal = ", (0, 700), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)
                        cv2.putText(img, str(u), (530, 700), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)
                        if fingers[4]:
                            cv2.rectangle(imgCanvas, (x0, y0), (x1, y1), drawColor)

                    #Circle
                    if shape == 'circle':
                        z1, z2 = lmList[4][1:]
                        # print(z1,z2)
                        result = int(((((z1 - x1) ** 2) + ((z2 - y1) ** 2)) ** 0.5))
                        # print(result)
                        if result < 0:
                            result = -1 * result
                        u = result
                        cv2.putText(img, "Radius Of Circe = ", (0, 700), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)
                        cv2.putText(img, str(u), (450, 700), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)
                        cv2.circle(img,(x0,y0),u,drawColor)
                        if fingers[4]:
                            cv2.circle(imgCanvas, (x0, y0), u, drawColor)



                    #Ellipse
                    if shape == 'ellipse':
                        z1, z2 = lmList[4][1:]
                        # cv2.ellipse(img,(x1,y1),(int(z1/2),int(z2/2)),0,0,360,255,0)
                        a = z1-x1
                        b= (z2-x2)
                        if x1 > 250:
                            b = int(b/2)
                        if a < 0:
                            a =-1*a
                        if b < 0:
                            b = -1*b

                        cv2.ellipse(img, (x1, y1),(a,b), 0, 0, 360, drawColor, 0)
                        cv2.putText(img, "Major AL, Minor AL = ", (0, 700), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 255), 3)
                        cv2.putText(img, str(a), (550, 700), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 255), 3)
                        cv2.putText(img, str(b), (700, 700), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 255), 3)
                        if fingers[4]:
                            cv2.ellipse(imgCanvas, (x1, y1), (a, b), 0, 0, 360, drawColor, 0)

                xp, yp = x1, y1

            # Clear Canvas when 2 fingers are up

            if fingers[2] and fingers[3] and fingers[0] == 0 and fingers[1] == 0 and fingers[4] == 0:
                imgCanvas = np.zeros((720, 1280, 3), np.uint8)

        imgGray = cv2.cvtColor(imgCanvas, cv2.COLOR_BGR2GRAY)
        _, imgInv = cv2.threshold(imgGray, 50, 255, cv2.THRESH_BINARY_INV)
        imgInv = cv2.cvtColor(imgInv, cv2.COLOR_GRAY2BGR)
        img = cv2.bitwise_and(img, imgInv)
        img = cv2.bitwise_or(img, imgCanvas)

        # Setting the header image
        img[0:70, 0:1280] = header
        # img = cv2.addWeighted(img,0.5,imgCanvas,0.5,0)

        cv2.imshow("Image", img)
        # cv2.imshow("Canvas", imgCanvas)
        # cv2.imshow("Inv", imgInv)
        cv2.waitKey(1)





virtual_Painter()




