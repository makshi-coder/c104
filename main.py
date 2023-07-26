import cv2
img=cv2.imread("butterfly.jpg")
grayimage=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
cv2.imshow("displayimage",grayimage)
print(grayimage)
cv2.waitKey(0)

