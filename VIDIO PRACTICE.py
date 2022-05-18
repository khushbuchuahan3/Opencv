import cv2
img=cv2.imread("friendsjpg.jpg")
capture=cv2.VideoCapture('highway.mp4')


def reduction(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimension = (width, height)
    return cv2.resize(frame, dimension, interpolation=cv2.INTER_AREA)


while True:
    isTrue,frame=capture.read()
    resize_vidio=reduction(frame)
    cv2.imshow("vidio",frame)
    cv2.imshow("resize",resize_vidio)
    if cv2.waitKey(30)& 0xFF==ord('d'):
        break
#############  for images
import cv2
import numpy as np

black = np.zeros((500, 500, 3), dtype="uint8")
# black[200:300,400:500]=0,255,0
rectangle = cv2.rectangle(black, (0, 0), (black.shape[1] // 2, black.shape[0] // 2), (255, 0, 0), cv2.FILLED)

# draw circle
cv2.circle(black, (250, 250), 50, (255, 255, 0), -1)
# draw line
cv2.line(black, (0, 0), (100, 100), (255, 255, 0), 5)

# put text
cv2.putText(black, "this is me ", (0,300), cv2.FONT_HERSHEY_PLAIN, 1,(255, 255, 255), 4)
cv2.imshow("black", black)
cv2.imshow("red", black)

cv2.waitKey(0)

capture.release()
cv2.destroyAllWindows()
