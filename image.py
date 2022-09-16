import cv2

img = cv2.imread('assets/logo.jpg', 1)

# RESIZE THE IMAGE
# img = cv2.resize(img , (400, 400))
img = cv2.resize(img, (0, 0), fx=0.2, fy=0.2)

# ROTATE THE IMAGE
img = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)

# print the customized image 
cv2.imwrite('new_image', img)

cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
