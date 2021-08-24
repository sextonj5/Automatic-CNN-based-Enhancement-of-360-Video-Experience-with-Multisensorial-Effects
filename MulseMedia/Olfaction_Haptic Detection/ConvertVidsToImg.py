import cv2
from PIL import Image
import winsound
#
#
#
vidcap = cv2.VideoCapture('j.mp4')
count = 9860
stop = 10000
def split(img):
    global count
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    im1 = Image.fromarray(img, 'RGB')
    im1.save(str(count).zfill(9)+".jpg")     # save frame as JPG file
    count += 1

def getFrame(sec):
    global count
    vidcap.set(cv2.CAP_PROP_POS_MSEC,sec*10)
    hasFrames,image = vidcap.read()
    if hasFrames:
        split(image)
    return hasFrames

sec = 3000 #start at 10 seconds to get rid of intro credits
frameRate = 10 # frame every x seconds
success = getFrame(sec)
while (success and count<=stop):
    sec = sec + frameRate
    sec = round(sec, 2)
    print(count)
    success = getFrame(sec)
duration = 1000  # milliseconds
freq = 440  # Hz
winsound.Beep(freq, duration)
    
    




