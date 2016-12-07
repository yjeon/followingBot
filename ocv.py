import cv2
import numpy as np



cap = cv2.VideoCapture(0)

while(1):

	# Take each frame
	_, frame = cap.read()
	if(_ == True):
		# Convert BGR to HSV
		hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
		# define range of blue color in HSV
		lower_blue = np.array([110,50,50])
		upper_blue = np.array([130,255,255])
		
		# Threshold the HSV image to get only blue colors
 		mask = cv2.inRange(hsv, lower_blue, upper_blue)
		# Bitwise-AND mask and original image
		res = cv2.bitwise_and(frame,frame, mask= mask)
		
		
		dst = cv2.inRange(res, lower_blue, upper_blue)
		no_blue = cv2.countNonZero(dst)
		print str(no_blue)
		
		
		cv2.imshow('Original',frame)
		#cv2.imshow('mask',mask)
		cv2.imshow('Only Blue',res)
		k = cv2.waitKey(5) & 0xFF
		if k == 27:
			break
cv2.destroyAllWindows()


'''# Standard imports
import cv2
import numpy as np;
 
# Read image
im = cv2.imread("blob.jpg", cv2.IMREAD_GRAYSCALE)
 
# Set up the detector with default parameters.
detector = cv2.SimpleBlobDetector()
 
# Detect blobs.
keypoints = detector.detect(im)
 
# Draw detected blobs as red circles.
# cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures the size of the circle corresponds to the size of blob
im_with_keypoints = cv2.drawKeypoints(im, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
 
# Show keypoints
cv2.imshow("Keypoints", im_with_keypoints)
cv2.waitKey(0)'''