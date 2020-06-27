

import cv2

face_cascade = cv2.CascadeClassifier("./App6/haarcascade_frontalface_default.xml")

img = cv2.imread("./App6/IMG_3829.jpg")

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray_img,
                                    scaleFactor=1.10,  #each iteraction recscales search down by 5%. Larger number less accurate
                                    minNeighbors=10)  # how many neighbours to search around.

print(faces)


border_thickness = 3
border_colour = (255,0,0)

for x, y, w, h in faces:
    img = cv2.rectangle(img, (x,y), (x+w,y+h), border_colour, border_thickness)

# img2[ (face[1]):( face[1] + border_thickness), face[0]:(face[0]+face[2]), :] = 0
# img2[ (face[1]+face[3]):(face[1]+face[3]+border_thickness), face[0]:(face[0]+face[2]), :] = 0
#
# img2[ face[1]:(face[1]+face[3]), (face[0]):( face[0] + border_thickness), :] = 0
# img2[ face[1]:(face[1]+face[3]), (face[0]+face[2]):(face[0]+face[2]+border_thickness), :] = 0

img_width = 1000
re_img = cv2.resize(img, (img_width, int(img.shape[0]/ img.shape[1] * img_width)) )

cv2.imshow("Test", re_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
