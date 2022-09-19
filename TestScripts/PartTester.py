import cv2 as cv
from utils import findFace

InPath = './BinaryData/FullPhoto.jpg'
img = cv.imread(InPath)
# img = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
pat = './BinaryData/haarcascade_frontalface_default.xml' #! path to xml file
img, info = findFace(img,pat)
cv.imshow("img",img)
cv.waitKey()
cv.destroyAllWindows()

