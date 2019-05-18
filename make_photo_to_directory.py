import cv2
import os
import os.path
import numpy as np
import cv2
import crop_photo

from align import AlignDlib
alignment = AlignDlib('models/landmarks.dat')

cam = cv2.VideoCapture(0)
cam2 = cv2.VideoCapture(1)

cv2.namedWindow("right")
cv2.namedWindow("left")


j = 0

path_photo = "photo\\"


print("directory:")
name = input()
if not os.path.exists(path+str(name)):
    os.makedirs(path+str(name))
if not os.path.exists(path_photo+str(name)):
    os.makedirs(path_photo+str(name))
    os.makedirs(path_photo+str(name) + "\\left")
    os.makedirs(path_photo+str(name) + "\\right")



while True:
    
    ret, frame_right = cam.read()
    ret2, frame_left = cam2.read()
    cv2.imshow("right", frame_right)
    cv2.imshow("left", frame_left)
    

    
    k = cv2.waitKey(1)
    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k%256 == 32:
        print("stop")
        name = input()


    # Load an image of Jacques Chirac
    jc_orig_left = frame_left
    jc_orig_right = frame_right
    
    # Detect face and return bounding box
    bb1 = alignment.getLargestFaceBoundingBox(jc_orig_left)
    bb2 = alignment.getLargestFaceBoundingBox(jc_orig_right)
    # Transform image using specified face landmark indices and crop image to 96x96
    jc_aligned1 = alignment.align(96, jc_orig_left, bb1, landmarkIndices=AlignDlib.OUTER_EYES_AND_NOSE)
    
    jc_aligned2 = alignment.align(96, jc_orig_right, bb2, landmarkIndices=AlignDlib.OUTER_EYES_AND_NOSE)
    if jc_aligned1 is None or jc_aligned2 is None:
        continue

    #make_magic
    j = j + 1

    cv2.imwrite(path_photo+str(name)+"\\left\\"+str(j)+".png",jc_orig_left)
    cv2.imwrite(path_photo+str(name)+"\\right\\"+str(j)+".png",jc_orig_right)
    
    print("saved: " + name + "  " + str(j))
    if j == 1500:
        break

    

cv2.destroyAllWindows()