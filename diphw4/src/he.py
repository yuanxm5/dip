from PIL import Image
from numpy import *
from pylab import *
from matplotlib import pyplot
from scipy.misc import lena, toimage

def histImageArr(im_arr, cdf):
    cdf_min = cdf[0]
    im_w = len(im_arr[0])
    im_h = len(im_arr)
    im_num = im_w*im_h
    color_list = []
    i=0
    while i<256:
        if i>len(cdf) - 1:
            color_list.append(color_list[i-1])
            break
        tmp_v = (cdf[i] - cdf_min)*255/(im_num-cdf_min)
        color_list.append(tmp_v)
        i += 1
    arr_im_hist = []
    for itemL in im_arr:
        tmp_line = []
        for item_p in itemL:
            tmp_line.append(color_list[item_p])
        arr_im_hist.append(tmp_line)
    return arr_im_hist

def beautyImage(im_arr):
    imhist, bins = histogram(im_arr.flatten(), range(256))
    cdf = imhist.cumsum()
    return histImageArr(im_arr, cdf)

def hist(im_source):
    arr_im_rgb  = array(im_source)
    arr_im_rcolor = []
    arr_im_gcolor = []
    arr_im_bcolor = []
    i = 0
    for itemL in arr_im_rgb:
        arr_im_gcolor.append([])
        arr_im_rcolor.append([])
        arr_im_bcolor.append([])
        for itemC in itemL:
            arr_im_rcolor[i].append(itemC[0])
            arr_im_gcolor[i].append(itemC[1])
            arr_im_bcolor[i].append(itemC[2])
        i = 1+i
    arr_im_rcolor_hist = beautyImage(array(arr_im_rcolor))
    arr_im_gcolor_hist = beautyImage(array(arr_im_gcolor))
    arr_im_bcolor_hist = beautyImage(array(arr_im_bcolor))
    i = 0
    arr_im_hist = []
    while i<len(arr_im_rcolor_hist):
        ii = 0
        tmp_line = []
        while ii < len(arr_im_rcolor_hist[i]):
            tmp_point = [arr_im_rcolor_hist[i][ii], arr_im_gcolor_hist[i][ii],arr_im_bcolor_hist[i][ii]]
            tmp_line.append(tmp_point)
            ii += 1
        arr_im_hist.append(tmp_line)
        i += 1

    figure()
    im_beauty = toimage(array(arr_im_hist), 255)
    im_beauty.show()
    im_beauty.save("../result/he/he_seperate.png")
