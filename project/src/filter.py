import numpy as np
from PIL import Image
from math import floor, ceil

def filter2d(input_img, filter, size = 3):
    imgheight, imgwidth = input_img.shape
    n, m = size, size
    a, b = m / 2, n / 2 
    def juanji(x, y):
        z = np.full(n * m, input_img[x, y]) 
        for i in range(x - a, x + a + 1):
            for j in range(y - b, y + b + 1):
                if i >= 0 and i < imgheight and j >= 0 and j < imgwidth:
                    z[(i - x + a) * n + j - y + b] = input_img[i, j]
        return np.dot(filter.ravel(), z)
    w, h = np.meshgrid(range(imgheight), range(imgwidth), indexing='ij')
    func = np.vectorize(juanji)
    return func(w, h)

def arithmetic_mean(input_img, size):
    filter = np.full((size, size), float(1) / (size * size))
    imgdata = np.asarray(input_img)
    #imgdata = np.array(input_img.getdata(), dtype=np.float64).reshape(input_img.size[::-1])
    arr = filter2d(imgdata, filter, size)
    return arr


def harmonic_mean(img, size):
    imgdata = np.array(img.getdata(), dtype=np.float64).reshape(img.size[::-1])
    #imgdata = np.asarray(img)
    reciprocal = np.reciprocal(imgdata)
    arr = np.reciprocal(arithmetic_mean(reciprocal, size))   
    return arr
    

def contraharmonic_mean(img, size, Q):
    imgdata = np.array(img.getdata(), dtype=np.float64).reshape(img.size[::-1])
    molecular = np.power(imgdata, Q+1)    
    denominator = np.power(imgdata, Q)    
    arr = arithmetic_mean(molecular, size) / arithmetic_mean(denominator, size)
    return arr
    Image.fromarray(arr).convert("L").save("../result/task_1/contraharmonic_mean" + str(size) + '_' + str(size) + ".png")

    
def static_filter(input_img, filtername, size = 3):
    imgheight, imgwidth = input_img.shape
    n, m = size, size
    a, b = m / 2, n / 2 
    def patch(x, y):
        z = np.full(n * m, input_img[x, y]) 
        for i in xrange(x - a, x + a + 1):
            for j in xrange(y - b, y + b + 1):
                if i >= 0 and i < imgheight and j >= 0 and j < imgwidth:
                    z[(i - x + a) * n + j - y + b] = input_img[i, j]
        if filtername == 'max':
            return z.max()
        elif filtername == 'min':
            return z.min()
        elif filtername == 'geometric':
            return np.prod(np.power(z, 1.0 / (m * n)))        
        else:
            return np.median(z)
    w, h = np.meshgrid(range(imgheight), range(imgwidth), indexing='ij')
    func = np.vectorize(patch)
    return func(w, h)
