import numpy as np
from PIL import Image
from noise_generator import *
from filter import *
from he import *

def test_average():
    img = Image.open("../img/task_1.png").convert("L")
    arr = arithmetic_mean(img, 3)
    Image.fromarray(arr).convert("L").save("../result/task_1/arithmetic_mean3_3.png")
    arr = arithmetic_mean(img, 9)
    Image.fromarray(arr).convert("L").save("../result/task_1/arithmetic_mean9_9.png")
    Image.fromarray(harmonic_mean(img, 3)).convert("L").save("../result/task_1/harmonic_mean3_3.png")
    Image.fromarray(harmonic_mean(img, 9)).convert("L").save("../result/task_1/harmonic_mean9_9.png")
    Image.fromarray(contraharmonic_mean(img, 3, -1.5)).convert("L").save("../result/task_1/contraharnic_mean3_3.png")
    Image.fromarray(contraharmonic_mean(img, 9, -1.5)).convert("L").save("../result/task_1/contraharnic_mean9_9.png")


def test_gauss():
    img = Image.open("../img/task_2.png").convert("L")    
    imgdata = np.array(img.getdata(), dtype=np.float64).reshape(img.size[::-1])
    arr = addGaussNoise(imgdata)    
    Image.fromarray(arr).convert("L").save("../result/task_2/gauss/gaussnoise.png")        
    noiseImg = Image.fromarray(arr).convert("L")
    Image.fromarray(arithmetic_mean(noiseImg, 3)).convert("L").save("../result/task_2/gauss/arithmetic_mean.png")
    Image.fromarray(harmonic_mean(noiseImg, 3)).convert("L").save("../result/task_2/gauss/harmonic_mean.png")
    Image.fromarray(contraharmonic_mean(noiseImg, 3, -1.5)).convert("L").save("../result/task_2/gauss/contraharnic_mean.png")
    Image.fromarray(static_filter(arr, 'meidan', 3)).convert("L").save("../result/task_2/gauss/median.png")
    Image.fromarray(static_filter(arr, 'geometric', 3)).convert("L").save("../result/task_2/gauss/geometric.png")

def test_salt():
    img = Image.open("../img/task_2.png").convert("L")    
    imgdata = np.array(img.getdata(), dtype=np.float64).reshape(img.size[::-1])
    arr = addSaltNoise(imgdata)
    Image.fromarray(arr).convert("L").save("../result/task_2/salt/saltnoise.png")    
    noiseImg = Image.fromarray(arr).convert("L")
    Image.fromarray(contraharmonic_mean(noiseImg, 3, 1.5)).convert("L").save("../result/task_2/salt/contraharnic_mean_pos.png")
    Image.fromarray(contraharmonic_mean(noiseImg, 3, -1.5)).convert("L").save("../result/task_2/salt/contraharnic_mean_neg.png")
    

def test_sap(): 
    img = Image.open("../img/task_2.png").convert("L")    
    imgdata = np.array(img.getdata(), dtype=np.float64).reshape(img.size[::-1])
    arr = addsapNoise(imgdata)
    Image.fromarray(arr).convert("L").save("../result/task_2/sap/sapnoise.png")
    noiseImg = Image.fromarray(arr).convert("L")
    Image.fromarray(arithmetic_mean(noiseImg, 3)).convert("L").save("../result/task_2/sap/arithmetic_mean.png")
    Image.fromarray(harmonic_mean(noiseImg, 3)).convert("L").save("../result/task_2/sap/harmonic_mean.png")
    Image.fromarray(contraharmonic_mean(noiseImg, 3, 1.5)).convert("L").save("../result/task_2/sap/contraharnic_mean.png")
    Image.fromarray(static_filter(arr, 'min', 3)).convert("L").save("../result/task_2/sap/min.png")
    Image.fromarray(static_filter(arr, 'max', 3)).convert("L").save("../result/task_2/sap/max.png")
    Image.fromarray(static_filter(arr, 'meidan', 3)).convert("L").save("../result/task_2/sap/median.png")

def test_he():
    img = Image.open("../img/91.png")
    #equalize_rgb_seperate(img).save("../result/he/he_seperate.png")
    #equalize_rgb_together(img).save("../result/he/he_together.png")
    hist(img)
    
if __name__ == "__main__":
    test_average()
    test_gauss()
    test_salt()
    test_sap()
    test_he()


