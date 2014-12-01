import numpy as np
from PIL import Image
from functions import *


def getFilter(filtername):
    if filtername == 'average':
        filter = np.full((266, 394), 0, dtype = np.int)
        for i in range(filter.shape[0]):
            for j in range(filter.shape[1]):
                if i < 11 and j < 11:
                    filter[i][j] = 1
    if filtername == 'laplacian':
        filter = np.full((258, 386), 0, dtype = np.int)
        for i in range(filter.shape[0]):
            for j in range(filter.shape[1]):
                if i < 3 and j < 3:
                    if i == 1 and j == 1:
                        filter[i][j] = 8
                    else:
                        filter[i][j] = -1
    filter = center(filter)
    return filter


def getPadding(data, filtername):
    if filtername == 'average':
        addNum = 5
    if filtername == 'laplacian':
        addNum = 1
    padding = np.full((256 + 2 * addNum, 384 + 2 * addNum), 0, dtype = np.int)
    for i in range(padding.shape[0]):
        for j in range(padding.shape[1]):
            if i >= addNum and i < padding.shape[0] - addNum and j >= addNum and j < padding.shape[1] - addNum:
                padding[i][j] = data[i - addNum][j - addNum]
    padding = center(padding)
    return padding        
    
def getOutdata(data, filtername):
    if filtername == 'average':
        return data[4:260, 5:389]
    if filtername == 'laplacian':
        return data[1:257, 2:386]
    

def filter2d_freq(input_img, filtername):
    data = np.asarray(input_img)                            
    data.setflags(write = True)
    filter = getFilter(filtername)
    dftOfFilter = np.asarray(get_DFT_matrix(filter))  
    padding = getPadding(data, filtername)
    dftdata = np.asarray(get_DFT_matrix(padding))
    multimatrix = np.asarray(dftOfFilter * dftdata)                                
    idftdata = np.asarray(get_IDFT_matrix(multimatrix))    
    idftdata = np.real(idftdata)
    idftdata = center(idftdata)
    if filtername == 'average':
        outdata = scale(idftdata)
    if filtername == 'laplacian' :
        outdata = scale(idftdata)
    outdata = getOutdata(outdata, filtername)
    print 'Saving ' + filtername + '.png in result folder'
    Image.fromarray(outdata).save('../result/' + filtername + '.png')
        
