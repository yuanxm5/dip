import numpy as np

from PIL import Image
from random import random
from math import sin, cos, log, sqrt, pi

def addGaussNoise(imgdata):
    img = Image.open("../img/task_2.png").convert("L")    
    noise = np.random.normal(0, 40, 464*448).reshape(img.size[::-1])
    return imgdata + noise
    arr = imgdata + noise
    Image.fromarray(arr).convert("L").save("../result/task_2/gauss/gauss-0-40.png")


def addSaltNoise(imgdata):
    def salt(data):
        if random() < 0.2:
            return 255
        else:
            return data
    func = np.vectorize(salt)
    arr = func(imgdata)
    return arr
    Image.fromarray(arr).convert("L").save("../result/task_2/salt/saltnoise.png")

    
def addsapNoise(imgdata):
    def sap(data):
        if random() < 0.2:
            return 255
        elif random() > 0.8:
            return 0
        else:
            return data
    func = np.vectorize(sap)
    arr = func(imgdata)
    return arr
    Image.fromarray(arr).convert("L").save("../result/task_2/sap/sapnoise.png")    

            
