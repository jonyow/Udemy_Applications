
import cv2
import datetime
import matplotlib.pyplot as plt

face_cascade = cv2.CascadeClassifier("./App6/haarcascade_frontalface_default.xml")

def runFaceClassifer(img):
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray_img,
                                    scaleFactor=1.10,  #each iteraction recscales search down by 5%. Larger number less accurate
                                    minNeighbors=10)  # how many neighbours to search around.

    border_thickness = 3
    border_colour = (255,0,0)

    print( "No. of faces: " + len(faces).__str__() )

    for x, y, w, h in faces:
        img = cv2.rectangle(img, (x,y), (x+w,y+h), border_colour, border_thickness)

    img_width = 1000
    re_img = cv2.resize(img, (img_width, int(img.shape[0]/ img.shape[1] * img_width)) )

    return(re_img, len(faces))

video = cv2.VideoCapture(0)

timestamps = []
num_faces_list = []

fig = plt.figure()

while True:
    check, frame = video.read()

    face_frame, num_faces  = runFaceClassifer(frame)

    timestamps.append( datetime.datetime.now().strftime("%H:%M:%S")  )
    num_faces_list.append(num_faces)

    plt.clf()
    plt.bar(timestamps, num_faces_list, 0.1, color='blue')
    fig.canvas.draw()

    cv2.imshow("Test", face_frame)

    key = cv2.waitKey(1000)

    if key ==ord("q"):
        break

# plt.clf()
# x =  ['A', 'B','C', 'D', 'E', "G"]
# y = [0,0,0,1,3,5]
# plt.bar(x,y, 1, color='blue')

video.release()
cv2.destroyAllWindows()
plt.close()


