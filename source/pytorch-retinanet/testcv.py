import cv2

image = cv2.imread('images/1.jpg',1)
cv2.imshow("keytest",image)
ret = cv2.waitKey(0)
print('pressed key is {0}'.format(ret))
