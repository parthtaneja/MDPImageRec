import cv2
import numpy as np
import glob

#empty list to store template images
template_data=[]
#make a list of all template images from a directory
files1= glob.glob('*.jpg')

for myfile in files1:
    image = cv2.imread(myfile,0)
    template_data.append(image)

test_image=cv2.imread('imagerectemplate.jpg')
#test_image= cv2.cvtColor(test_image, cv2.COLOR_BGR2GRAY)

#loop for matching
for tmp in template_data:
    (tH, tW) = tmp.shape[:2]
    cv2.imshow("Template", tmp)
    cv2.waitKey(1000)
    cv2.destroyAllWindows()
    result = cv2.matchTemplate(test_image, tmp, cv2.TM_CCOEFF)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    top_left = max_loc
    bottom_right = (top_left[0] + tW, top_left[1] + tH)
    cv2.rectangle(test_image,top_left, bottom_right,255, 2)

cv2.imshow('Result',test_image)
cv2.waitKey(0)
