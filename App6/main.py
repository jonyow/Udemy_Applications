
import cv2

img = cv2.imread("./App6/galaxy.jpg", 0)

resized_img = cv2.resize(img, (int(img.shape[0]/2),int(img.shape[1]/2)))
cv2.imshow("Galxy", resized_img)

cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite("galaxy2.jpg", resized_img)