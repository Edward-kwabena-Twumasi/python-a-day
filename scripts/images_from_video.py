# Importing all necessary libraries 
import cv2 
import os 
from pathlib import Path as path

# Read the video from specified path 
media_path = path("../../Media/globe.mp4")
cam = cv2.VideoCapture("../../Media/globe.mp4") 

try: 
	
	# creating a folder named data 
	if not media_path.exists(): 
		os.makedirs('data') 

# if not created then raise error 
except OSError: 
	print ('Error: Creating directory of data') 

# frame 
currentframe = 0

while(currentframe<50): 
	      
	# reading from frame 
	ret,frame = cam.read()
	print("ret {} / frame {}".format(ret,frame))
	pass 
   
	if ret: 
		# if video is still left continue creating images 
		name = './data/{}{}.jpg'.format(media_path.name.split('.')[0],str(currentframe))
		print ('Creating...' + name) 

		# writing the extracted images 
		cv2.imwrite(name, frame) 

		# increasing counter so that it will 
		# show how many frames are created 
		currentframe += 1
	else: 
		break

# Release all space and windows once done 
cam.release() 
cv2.destroyAllWindows() 
