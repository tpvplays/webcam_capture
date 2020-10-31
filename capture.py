import cv2
import numpy as np


video_capture = cv2.VideoCapture(1)
##CODEC
fourcc = cv2.cv.CV_FOURCC(*'XVID')
video_out = cv2.VideoWriter('recorded.avi', fourcc, 20.0, (640,480))


while True:

	cap, frame = video_capture.read()
	cv2.imshow("Capturing", frame)
	video_out.write(frame)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break


video_capture.release()
video_out.release()