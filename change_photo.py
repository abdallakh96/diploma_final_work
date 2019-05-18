import os
import os.path
import numpy as np
import cv2
import crop_photo

from align import AlignDlib
def load_image(path):
    img = cv2.imread(path, 1)
    # OpenCV loads images with color channels
    # in BGR order. So we need to reverse them
    return img

path = 'photo\\'
path_res = 'dataset\\'
alignment = AlignDlib('models/landmarks.dat')
#photo\camera2

directories = os.listdir(path)

for directory in directories:
    #print(directory)
    i = 1
    j = 0
    if not os.path.exists(path_res+str(directory)):
        os.makedirs(path_res+str(directory))
        
    for i in range(0,1500):
        left_photo_path = path + directory + "\\left\\" + str(i) + ".jpg"
        right_photo_path = path + directory + "\\right\\" + str(i) + ".jpg"
        
        if os.path.exists(left_photo_path) and os.path.exists(right_photo_path):

            left = load_image(left_photo_path)
            right = load_image(right_photo_path)


            # Load an image of Jacques Chirac
            jc_orig_left = load_image(left_photo_path)
            jc_orig_right = load_image(right_photo_path)
            # Detect face and return bounding box
            bb1 = alignment.getLargestFaceBoundingBox(jc_orig_left)
            bb2 = alignment.getLargestFaceBoundingBox(jc_orig_right)
            # Transform image using specified face landmark indices and crop image to 96x96
            jc_aligned_left = alignment.align(96, jc_orig_left, bb1, landmarkIndices=AlignDlib.OUTER_EYES_AND_NOSE)
            
            jc_aligned_right = alignment.align(96, jc_orig_right, bb2, landmarkIndices=AlignDlib.OUTER_EYES_AND_NOSE)
            if jc_aligned_left is None or jc_aligned_right is None:
                continue

            #make_magic
            j = j + 1
            res = np.concatenate((jc_aligned_left, jc_aligned_right), axis=2)
            np.save( path_res+str(directory) + "\\"+str(j),res)
            print("saved: " + directory + str(j))
                
    
        
'''os.path.exists(file_path)'''