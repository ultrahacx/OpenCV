import cv2

img = cv2.imread('test.jpg', 0)
cv2.imshow('Image', img)
ah= cv2.waitKey(0)

if ah == 27:
    cv2.destroyAllWindows()



