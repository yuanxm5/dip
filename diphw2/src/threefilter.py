from PIL import Image
import numpy as np

def filter2d(input_img, filter, size = 3):
    newimg = Image.new(input_img.mode, input_img.size)
    data = list(input_img.getdata())
    pixels = np.reshape(data, (input_img.size[1], input_img.size[0]))
    a = size/2
    b = size/2
    imgheight, imgwidth = input_img.size
    if filter == 'average':
        weight = np.full(size*size, float(1)/(size*size))
    if filter == 'laplacian':
        laplacian = np.array([[-1, -1, -1],
                              [-1,  8, -1],
                              [-1, -1, -1]])
        
        weight = laplacian.flatten()
    if filter == 'sobel1':
        sobel1 = np.array([[-1, -2, -1],
                           [0,  0,  0],
                           [1,  2,  1]])
        weight = sobel1.flatten()
    if filter == 'sobel2':
        sobel2 = np.array([[-1, 0, 1],
                           [-2, 0, 2],
                           [-1, 0, 1]])
        weight = sobel2.flatten()
    for y in range(input_img.size[1]):
        for x in range(input_img.size[0]):                
            z = np.full(size * size, pixels[y][x])
            for j in range(y - a, y + a + 1):
                for i in range(x - b, x + b + 1):
                    if i > 0 and i < imgheight and j > 0 and j < imgwidth:
                        z[(j - y + a) * size + i - x + b] = pixels[j][i]
            newimg.putpixel((x, y), np.dot(weight, z))
    return newimg
    
        
    
