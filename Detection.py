import cv2
file = input("Input filename >>> ")

img = cv2.imread(file)
imgContour = img.copy()
img= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
canny = cv2.Canny(img,150,200)
contours,hierarchy = cv2.findContours(canny,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)

for cnt in contours:
    cv2.drawContours(imgContour,cnt,-1,(255,0,0),4)
    area = cv2.contourArea(cnt)
    if area > 500:
        peri = cv2.arcLength(cnt,True)
        vertices = cv2.approxPolyDP(cnt,peri*0.02,True)
        corners = (len(vertices))
        x,y,w,h = cv2.boundingRect(vertices)
        cv2.rectangle(imgContour,(x,y),(x+w,y+h),(0,255,0),4)
        if corners == 3:
            cv2.putText(imgContour,'Triangle',(x,y-5),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2) 
        elif corners == 4:
            cv2.putText(imgContour,'Rectangle',(x,y-5),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)
        elif corners == 5:
            cv2.putText(imgContour,'Pentagon',(x,y-5),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)
        elif corners == 6:
            cv2.putText(imgContour,'Hexagon',(x,y-5),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)
        elif corners == 7:
            cv2.putText(imgContour,'Heptagon',(x,y-5),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)
        elif corners == 8:
            cv2.putText(imgContour,'Octagon',(x,y-5),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)
        elif corners == 9:
            cv2.putText(imgContour,'Nonagon',(x,y-5),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)
        elif corners == 10:
            cv2.putText(imgContour,'Decagon',(x,y-5),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)


cv2.imshow('img',img)
cv2.imshow('canny',canny)
cv2.imshow('imgContour',imgContour)
cv2.waitKey(0)
