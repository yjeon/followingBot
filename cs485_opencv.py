import cv2
import numpy as np
import sys
import create

ACCEPTANCE_RANGE = 30
BOX_SIZE = 100
def rangeConverter(oldMin, oldMax, newMin, newMax, oldValue):
	oldRange = oldMax - oldMin
	newRange = newMax - newMin
	newValue = (((oldValue - oldMin) * newRange) / oldRange) + newMin
	return newValue
	
def gimpToHSV(h, s, v):

	result = []
	openCV_hLow = openCV_sLow = openCV_vLow = 0
	openCV_hHigh = 180
	openCV_sHigh = 255
	openCV_vHigh = 255
	
	gimp_hLow = gimp_sLow = gimp_vLow = 0
	gimp_hHigh = 360
	gimp_sHigh = 100
	gimp_vHigh = 100	
	
	hConv = rangeConverter(gimp_hLow, gimp_hHigh, openCV_hLow, openCV_hHigh, h)
	hLower = int(hConv - ACCEPTANCE_RANGE)
	if(hLower < openCV_hLow):
		hLower = openCV_hLow
	hHigher = int(hConv + ACCEPTANCE_RANGE)
	if(hHigher > openCV_hHigh):
		hHigher = openCV_hHigh
	
	sConv = rangeConverter(gimp_sLow, gimp_sHigh, openCV_sLow, openCV_sHigh, s)
	sLower = int(sConv - ACCEPTANCE_RANGE)
	if(sLower < openCV_sLow):
		sLower = openCV_sLow
	sHigher = int(sConv + ACCEPTANCE_RANGE)
	if(sHigher > openCV_sHigh):
		sHigher = openCV_sHigh
	
	vConv = rangeConverter(gimp_vLow, gimp_vHigh, openCV_vLow, openCV_vHigh, v)
	vLower = int(vConv - ACCEPTANCE_RANGE)
	if(vLower < openCV_vLow):
		vLower = openCV_vLow
	vHigher = int(vConv + ACCEPTANCE_RANGE)
	if(vHigher > openCV_vHigh):
		vHigher = openCV_vHigh
	result.append([hLower, sLower, vLower])
	result.append([hHigher, sHigher, vHigher])
	return result
	
def getGimpValuesFromUser():
	h = int(raw_input("H: "))
	s = int(raw_input("S: "))
	v = int(raw_input("V: "))
	return [h,s,v]


def main():
	#Get gimp HSV values from user and convert to openCV HSV values
	h,s,v = getGimpValuesFromUser()
	upperAndLower = gimpToHSV(h, s, v)
	print "Upper:"
	print upperAndLower[0]
	print "Lower:"
	print upperAndLower[1]
	
	r = create.Create("/dev/ttyUSB0")
	cap = cv2.VideoCapture(0)
	while(1):
		# Take each frame
		_, frame = cap.read()
		if(_ == True):
			# Convert BGR to HSV
			hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
			lower_color = np.array(upperAndLower[0], np.uint8)
			upper_color = np.array(upperAndLower[1], np.uint8)
			
			# Threshold the HSV image to get only the color needed
			mask = cv2.inRange(hsv, lower_color, upper_color)
			# Bitwise-AND mask and original image
			res = cv2.bitwise_and(frame,frame, mask= mask)
			size = cv2.countNonZero(mask)
			print str(size)

			#TODO: we need to figure out how many value robot moves
			if(size<10000):
				r.setWheelVelocities(0,0)
			elif(size<30000):
				r.setWheelVelocities(5,5)
			else:
				r.setWheelVelocities(-5,-5)
			# Draw box on images
			height, width = frame.shape[:2]
			cv2.rectangle(frame,(320-BOX_SIZE,240+BOX_SIZE),(320+BOX_SIZE,240-BOX_SIZE),(0,255,0),1)
			cv2.rectangle(res,(320-BOX_SIZE,240+BOX_SIZE),(320+BOX_SIZE,240-BOX_SIZE),(0,255,0),1)
			
			cv2.imshow('Original',frame)
			cv2.imshow('One Color Only',res)
			k = cv2.waitKey(5) & 0xFF
			if k == 27:
				break
	cv2.destroyAllWindows
	
main()