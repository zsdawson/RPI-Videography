from time import sleep
import datetime as dt
import picamera
from subprocess import call

camera = picamera.PiCamera(resolution=(1024,768)) #about 1.8 Gb per hour recording under good lighting

camera.start_preview(alpha=200)

camera.annotate_background = picamera.Color('black')
camera.annotate_text_size = 50
camera.annotate_text = dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

vlength = 60 #length of each video.seconds
imax = 3 #number of total video clips

sleep(60) #time before the recording start.seconds

camera.start_recording('/media/pi/LaCie SSD/1.h264')
start = dt.datetime.now()
while (dt.datetime.now() - start).seconds < vlength:
    camera.annotate_text = dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    camera.wait_recording(0.2)

for i in range (2,imax+1):
    camera.split_recording('/media/pi/LaCie SSD/%d.h264' % i)
    start = dt.datetime.now()
    while (dt.datetime.now() - start).seconds < vlength:
        camera.annotate_text = dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        camera.wait_recording(0.2)

camera.stop_recording()
camera.stop_preview()

#call("sudo shutdown --poweroff", shell=True) #poweroff after recording
