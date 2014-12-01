import numpy as np
from cmath import exp, pi, sqrt
from PIL import Image


def DFT_matrix(N):
    i, j = np.meshgrid(np.arange(N), np.arange(N))    
    omega = np.exp( - 2 * pi * 1J / N )
    W = np.power( omega, i * j )
    return np.asmatrix(W)

def IDFT_matrix(N):
    i, j = np.meshgrid(np.arange(N), np.arange(N))    
    omega = np.exp( 2 * pi * 1J / N )
    W = np.power( omega, i * j )
    return np.asmatrix(W)

def get_DFT_matrix(data):
    return DFT_matrix(data.shape[0]) * data * DFT_matrix(data.shape[1])

def get_IDFT_matrix(data):
    return (1.0 / data.size) * IDFT_matrix(data.shape[0]) * data * IDFT_matrix(data.shape[1])

def scale(data):
    newdata = 255 * ((data - np.min(data)) / (np.max(data) - np.min(data)))
    arr = newdata.astype('uint8')
    return arr

def scale_t(data):
    newdata = 255 * data / np.max(data)
    arr = newdata.astype('uint8')
    return arr


def center(data):
    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            data[i][j] = data[i][j] * np.power(-1, i+j)
    return data
