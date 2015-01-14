from PIL import Image
import numpy as np
from filter import *

def getdivide(arr, content):
    return (arr / content)

def getMin(arr, content = np.array([1, 1, 1])):
    return np.array([min(getdivide(item, content)) for item in arr])
        
def getMax(arr):
    return np.array([max(item) for item in arr])

def test_dehaze_09CVPR():
    img = Image.open("../img/IMG_8763.jpg")    
    size = img.size[0] * img.size[1]
    flag = np.round(0.001 * size)
    data = np.asarray(img)
    M_x = np.array([getMin(row) for row in data])
    M_ave_x = static_filter(M_x, 'min', 15)
    #M_av = np.average(M_ave_x) / 255
    #omega = 0.75 / M_ave
    temp = M_ave_x.ravel().sort()    
    darkchannal_sort = M_ave_x.ravel()
    valve = darkchannal_sort[flag]
    
    #print valve
    Max = ([0,0,0], 0)
    rgb_itensity = []
    for i in range(img.size[1]):
        for j in range(img.size[0]):
            if M_ave_x[i][j] <= valve:                
                a = (data[i][j], sum(data[i][j]))
                #rgb_itensity.append(a)
                if a[1] >= Max[1]:
                    Max = a
                
    A = np.asarray(Max[0], dtype = float)
    I_divide_A = np.array([getMin(row, A) for row in data])
    #print M_I_divide_A
    M_I_divide_A = static_filter(I_divide_A, 'min', 15)
    t_x = np.asarray(1 - 0.95 * M_I_divide_A)
    
    newdata = []
    for i in range(img.size[1]):
        temp = []
        for j in range(img.size[0]):
            pixel = ((data[i][j] - A) / max(t_x[i][j], 0.1)) + A
            temp.append(pixel)
        newdata.append(temp)
    newdata = np.asarray(newdata, dtype = np.uint8)
    outimg = Image.fromarray(newdata, 'RGB')
    outimg.save("../result/dehaze-aaa.png")
    #Image.fromarray(M_ave_x).convert("L").save("../result/canon7-darkchannal.png")
    

if __name__ == "__main__":
    test_dehaze_rgb()
