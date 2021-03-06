#imports for packages
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageFilter, ImageEnhance
#import internal packages
from rockstarlifestyle import fouriertransform, preprocessing



#Function 1: Test of Magnitude_Spectrum function from fouriertransform
def test_Magnitude_Spectrum():
    """Test: peforms the fourier transform and returns the fshift which is used within filter functions"""
    #inputs for functions
    image = Image.open('../data/protein_matrix_image.png').convert('L')
    #function performance
    m_spec = fouriertransform.Magnitude_Spectrum(image)
    #asserts and checks
    assert isinstance(image, Image.Image), "input is in the wrong form"
    assert isinstance(m_spec, np.ndarray), "output is in the wrong form"
    return m_spec

#Function 2: Test of fourier_fshift from fouriertransform
def test_fourier_fshift():
    """Test: performs the fourier transform and returns the fshift which is used within filter functions"""
    #inputs for functions
    image = Image.open('../data/protein_matrix_image.png').convert('L')
    #function performance
    fshift = fouriertransform.fourier_fshift(image)
    #asserts and checks
    assert isinstance(image, Image.Image), "input is in the wrong form"
    assert isinstance(fshift, np.ndarray), "output is in the wrong form"
    return fshift
