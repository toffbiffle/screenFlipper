'''
Created by: Johan "Hishi" Persson
Created: 2023-09-13
'''
import cv2, pyautogui as pyag, numpy as np

try:
	while True:
		#MousePointer position x,y
		mousePos_x, mousePos_y = pyag.position()
	
		#Specify a capture area/mousepointer
		screenshot = pyag.screenshot( region=( mousePos_x-200, mousePos_y-100, 400, 200 )  )
		openCVPicture = np.array(screenshot)

		#Flip it
		openCVPicture = cv2.flip( openCVPicture, 1 )

		#Show the flipped image
		cv2.imshow( 'FlipIt', openCVPicture )
		
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break
except:
	print( "Something went wrong." )
	
#Close all
cv2.destroyAllWindows()
