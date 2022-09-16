import cv2
import random

img = cv2.imread('assets/logo.jpg', -1)

# print(img)
# print(img.shape) (height, width, channels)
# print(type(img))
# print(img[280] [400])

#CHANGE A PART OF THE IMAGE
# for i in range(100) :
#     for j in range(img.shape[1]) :
#         img[i][j] = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]


# CROP A PART OF THE IAMGE 
crop = img[ 350:650, 400:620]
img[200:500, 500:720] = crop

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()