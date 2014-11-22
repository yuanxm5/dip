import os
import argparse
import matplotlib
import numpy as np
import matplotlib.pyplot as plt

from threefilter import filter2d
from random import randint
from PIL import Image
from itertools import takewhile
from numpy import array
from skimage import data, img_as_float
from skimage import exposure

matplotlib.rcParams['font.size'] = 8

def equalize(data, total, level=256):
    pdf = map(lambda x: (x[1], float(x[0])/total), data)
    cdf = [sum(map(lambda x: x[1], takewhile(lambda x: x[0] <= i, pdf))) for i in range(level)]
    pixels = [round((level - 1) * i) for i in cdf]
    return pixels

def equalize_hist(input_img):
    colors = input_img.getcolors()
    numofPixels = input_img.size[0] * input_img.size[1]
    pixels = equalize(colors, numofPixels)
    output_img = Image.new(input_img.mode, input_img.size)
    for y in range(input_img.size[1]):
        for x in range(input_img.size[0]):
            output_img.putpixel((x, y), pixels[input_img.getpixel((x, y))])
    return output_img

def plot_img_and_hist(img, axes, bins=256):
    img = img_as_float(img)
    ax_img, ax_hist = axes
    ax_cdf = ax_hist.twinx()
    ax_img.imshow(img, cmap=plt.cm.gray)
    ax_img.set_axis_off()
    ax_hist.hist(img.ravel(), bins=bins, histtype='step', color='black')
    ax_hist.ticklabel_format(axis='y', style='scientific', scilimits=(0, 0))
    ax_hist.set_xlabel('Pixel intensity')
    ax_hist.set_xlim(0, 1)
    ax_hist.set_yticks([])
    img_cdf, bins = exposure.cumulative_distribution(img, bins)
    ax_cdf.plot(bins, img_cdf, 'r')
    ax_cdf.set_yticks([])
    return ax_img, ax_hist, ax_cdf

def plot_hist(input_img1, input_img2):
    img1 = array(input_img1.convert('L'))
    img2 = array(input_img2.convert('L'))
    p2, p98 = np.percentile(img1, (2, 98))    
    fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(8, 5))
    ax_img, ax_hist, ax_cdf = plot_img_and_hist(img1, axes[:, 0])
    ax_img.set_title('Original image')
    y_min, y_max = ax_hist.get_ylim()
    ax_hist.set_ylabel('Number of pixels')
    ax_hist.set_yticks(np.linspace(0, y_max, 5))
    ax_img, ax_hist, ax_cdf = plot_img_and_hist(img2, axes[:, 1])
    ax_img.set_title('Histogram equalization')
    ax_cdf.set_ylabel('Fraction of total intensity')
    ax_cdf.set_yticks(np.linspace(0, 1, 5))
    fig.subplots_adjust(wspace=0.4)
    fig.savefig('../result/plot.png')

def findPatch(input_img, width, height, key):
    data = list(input_img.getdata())
    pixels = np.reshape(data, (input_img.size[0], input_img.size[1]))
    x = key / (input_img.size[0] - width + 1)
    y = key % (input_img.size[0] - width + 1)
    return pixels[x:x + height, y:y + width]

def view_as_window(input_img, width, height):
    out = Image.new(input_img.mode, (width, height))
    xrandom = randint(0, input_img.size[0] - width)
    yrandom = randint(0, input_img.size[1] - height)
    for y in range(yrandom, yrandom + height):
        for x in range(xrandom, xrandom + width):
            out.putpixel((x - xrandom, y - yrandom), input_img.getpixel((x, y)))
    return out    
   
def main():
    input_img = Image.open('../img/91.png')
    output_img = equalize_hist(input_img)
    plot_hist(input_img, output_img)
    output_img.save('../result/histogramEqu.png')
    filter2d(input_img, 'average', 3).save('../result/averageFilter_3_3.png')
    filter2d(input_img, 'average', 7).save('../result/averageFilter_7_7.png')
    filter2d(input_img, 'average', 11).save('../result/averageFilter_11_11.png')
    filter2d(input_img, 'laplacian').save('../result/laplacian.png')
    filter2d(input_img, 'sobel1').save('../result/sobel_1.png')
    filter2d(input_img, 'sobel2').save('../result/sobel_2.png')
    for i in range(8):
        view_as_window(input_img, 96, 64).save('../result/viewAsWindow_96_64_' + str(i+1) + '.png')
        view_as_window(input_img, 50, 50).save('../result/viewAsWindow_50_50_' + str(i+1) + '.png')

if __name__ == "__main__":
    main()
