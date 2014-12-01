import numpy as np
from cmath import exp, pi, sqrt
from PIL import Image
from filter import filter2d_freq
from functions import *
from fft import *


def test_dft():
    input_img = Image.open("../img/91.png").convert('L')
    data = np.asarray(input_img)
    data.setflags(write = True)
    data = center(data)
    dftdata = np.asarray(get_DFT_matrix(data))
    outdata = scale(np.log10(np.abs(dftdata) ** 2))
    print 'Saving dft_center.png in result folder'
    Image.fromarray(outdata).save('../result/dft_center.png')
    test_idft(dftdata)
         

def test_idft(data):
    idftdata = np.asarray(get_IDFT_matrix(data))
    idftdata = np.real(idftdata)
    idftdata = center(idftdata)
    outdata = scale_t(idftdata)    
    print 'Saving idft.png in result folder'
    Image.fromarray(outdata).save('../result/idft.png')
    

def test_filter():
    input_img = Image.open("../img/91.png").convert('L')
    filter2d_freq(input_img, 'average')
    filter2d_freq(input_img, 'laplacian')

def main():
    test_dft()
    test_filter()
    print "Please ignore the warning, I tried my best to find the bug but failed"
    print "***************************************************"
    test_fft()
    test_ifft()


if __name__ == "__main__":
    main();

