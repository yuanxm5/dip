import numpy as np
import numpy
from cmath import exp, pi, sqrt
from PIL import Image
from functions import *

def DFT_slow(x):
    """Compute the discrete Fourier Transform of the 1D array x"""
    x = np.asarray(x, dtype=float)
    N = x.shape[0]
    n = np.arange(N)
    k = n.reshape((N, 1))
    M = np.exp(-2j * np.pi * k * n / N)
    return np.dot(M, x)

def FFT_1d(x):
    x = np.asarray(x, dtype = complex)
    N = x.shape[0]
    if N % 2 > 0:
        raise ValueError("size of x must be a power of 2")
    elif N <= 16:  
        return DFT_slow(x)
    else:
        X_even = FFT_1d(x[::2])
        X_odd = FFT_1d(x[1::2])
        factor = np.exp(-2j * np.pi * np.arange(N) / N)
        return np.concatenate([X_even + factor[:N / 2] * X_odd,
                               X_even + factor[N / 2:] * X_odd])

def FFT_2d(data):
    result = np.asarray(data)
    result = np.array([FFT_1d(row) for row in result])
    result = np.array([FFT_1d(col) for col in result.T])
    return result.T


def get_ifft(data):
    Fstar = np.conj(data)
    fstar = FFT_2d(Fstar) / reduce(np.multiply, data.shape, 1.0)
    return np.conj(fstar)


def test_fft():
    img = Image.open("../img/91.png").convert("L")
    data = np.asarray(img)
    data.setflags(write = True)
    data = center(data)
    fftdata = np.asarray(FFT_2d(data))
    outdata = scale(np.log10(np.abs(fftdata) ** 2))
    print "***************************************************"   
    print 'Saving fft_center.png in result folder'
    Image.fromarray(outdata).save('../result/fft_center.png')
    
def test_ifft():
    img = Image.open("../img/91.png").convert("L")
    data = np.asarray(img)
    data.setflags(write = True)
    ifftdata = get_IDFT_matrix(get_DFT_matrix(data))
    ifftdata = np.real(ifftdata)
    outdata = scale_t(ifftdata)    
    print 'Saving ifft.png in result folder'
    Image.fromarray(outdata).save('../result/ifft.png')

    

if __name__ == "__main__":
    test_fft()
    test_ifft()
    
