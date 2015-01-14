from PIL import Image
import numpy as np
import os.path

from filter import *

def getMin(arr):
    return np.array([min(item) for item in arr])
        
def getMax(arr):
    return np.array([max(item) for item in arr])

def test_dehaze_rgb(inputfile):
    img = Image.open("../img/" + inputfile)    
    data = np.asarray(img)
    M_x = np.array([getMin(row) for row in data])
    maxarr = np.array([getMax(row) for row in data])
    M_ave_x = arithmetic_mean(M_x, 7)
    #M_ave_x = static_filter(M_x, 'min', 15)
    M_av = np.average(M_ave_x) / 255
    omega = 0.8 / M_av
    #Image.fromarray(M_ave_x).convert("L").save("../result/canon7-darkchannal.png")
    La_x = []
    for i in range(img.size[1]):
        temp = []
        for j in range(img.size[0]):
            x = min(omega*M_av, 0.9) * M_ave_x[i][j]  
            y = min(x, M_x[i][j])
            temp.append(y)
        La_x.append(temp)
    La_x = np.array(La_x)
    #Image.fromarray(La_x).convert("L").save("../result/aaadark2.png")
    T = np.matrix([1,1,1]).T
    A = 0.5 * (max(maxarr.ravel()) + max(M_ave_x.ravel())) * T
    newdata = []
    for i in range(img.size[1]):
        temp = []
        for j in range(img.size[0]):
            fenzi = data[i][j] - La_x[i][j]
            fenmu = 1 - La_x[i][j]/A
            result = np.asarray(fenzi / fenmu)
            '''if i == 0 and j < 10:
                result = np.asarray(fenzi / fenmu)
                print result[0]'''
            temp.append(result[0])
        newdata.append(temp)
    newdata = np.asarray(newdata, dtype = np.uint8)
    #newdata = np.round(newdata)
    outimg = Image.fromarray(newdata, 'RGB')
    outimg.save("../result/dehaze-opt/dehaze-" + inputfile)
