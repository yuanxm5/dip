from PIL import Image
import numpy as np
import os.path

from filter import *
from dehaze_opt import *
from dehaze_09CVPR import *    

if __name__ == "__main__":
    filelist = os.listdir("../img")
    for img in filelist:
        test_dehaze_rgb(img)
        test_dehaze_09CVPR(img)
    #test_dehaze_rgb('IMG_8763.jpg')
    
