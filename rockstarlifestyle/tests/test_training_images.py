#import external packages
import numpy as np
import pandas as pd
from PIL import Image, ImageDraw
from random import randint
#import function packages
from rockstarlifestyle import training_images

#From training_images function folder:

#Function 1: Test of image generator for the circles image
#Image_training_circles
def test_im_gen_circles():
    """Test: Generates images with random circles on a background"""
    #function Inputs
    n = 2
    #function performance
    imgarray = training_images.im_gen_circles(n)
    #checks and asserts
    assert isinstance(n, int), "input is the wrong form"
    assert isinstance(imgarray, list), "output is in the wrong form"
    return imgarray

#Function 2: Test of the pixel counter for a circles image
def test_pix_count_im_circles():
    """Test: Counts the number of pixels for individual circle images"""
    #function Inputs
    n = 2
    array = training_images.im_gen_circles(n)
    array_index = 1
    #function performance
    black, obj_normalized = training_images.pix_count_im_circles(array, array_index)
    #checks and asserts
    assert isinstance(array_index, int), "Input is in the wrong form"
    assert isinstance(array, list), "Input is the wrong form"
    assert isinstance(black, int), "Output is the wrong form"
    #assert isinstance(obj_normalized, int), "Output is the wrong form"
    assert obj_normalized >= 1, "no objects were created"
    assert black + obj_normalized * 69 == 62500, "the total pixel number is not correct"
    return

#Function 3: Test of the pixel counter for all circle arrays
def test_pixel_counter_whole_array_circles():
    """Test: Counts the number of pixels for the array of circle images"""
    #function Inputs
    n = 2
    array = training_images.im_gen_circles(n)
    #function performance
    pixel_count = training_images.pix_count_array_circles(array)
    #checks and asserts
    assert isinstance(n, int), "input is the wrong form"
    assert isinstance(array, list), "input is in the wrong form"
    #assert pixel_count[1,1] + pixel_count[1,2]*69 == pixel_count[1,3],
    #"the total is incorrect"
    #assert pixel_count[3] == 62500, "the total is incorrect"
    #assert isinstance(pixel_count, pd.Dataframe), "output is in the
    #wrong form"
    return pixel_count


#From Image Training Pixels function filter
#Function 4: Test of random image pixel generator
def test_rand_im_gen():
    """Test: Generates images with randomized white pixels"""
    #function Inputs
    n = 2
    #function performance
    imgarray = training_images.rand_im_gen(n)
    #checks and asserts
    assert isinstance(n, int), "input is the wrong form"
    assert isinstance(imgarray, list), "output is in the wrong form"
    return imgarray

#Function 5: Test of random pixel counter
def test_pix_count_im():
    """Counts the number of colored pixels for a single image"""
    #function Inputs
    n = 2
    array = training_images.rand_im_gen(n)
    array_index = 1
    #function performance
    black, obj = training_images.pix_count_im(array, array_index)
    #checks and asserts
    assert isinstance(array_index, int), "Input is in the wrong form"
    assert isinstance(array, list), "Input is the wrong form"
    assert obj >= 1, "no objects were created"
    assert black + obj == 62500, "the total pixel number is not correct"
    return black, obj


#Function 6: Test of random pixel counter for whole array
def test_pix_count_array():
    """Test: Counts the number of colored pixels for a single image"""
    #function Inputs
    n = 2
    array = training_images.rand_im_gen(n)
    #function performance
    pixel_count = training_images.pix_count_array(array)
    #checks and asserts
    assert isinstance(n, int), "input is the wrong form"
    assert isinstance(array, list), "input is in the wrong form"
    return pixel_count




#Function 7: Test of image rectangle generator
def test_im_gen_rect():
    """Test: Generates a number of images with random rectangles"""
    #function Inputs
    n = 2
    #function performance
    imgarray = training_images.im_gen_rect(n)
    #checks and asserts
    assert isinstance(n, int), "input is the wrong form"
    assert isinstance(imgarray, list), "output is in the wrong form"
    return imgarray

#Function 8: Test of pixel counter for a rectangle image
def test_pix_count_im_rect():
    """Test: Counts the number of pixels in individual rectangle images"""
    #function Inputs
    n = 2
    array = training_images.im_gen_rect(n)
    array_index = 1
    #function performance
    black, obj_normalized = training_images.pix_count_im_rect(
                                            array, array_index)
    #checks and asserts
    assert isinstance(array_index, int), "Input is in the wrong form"
    assert isinstance(array, list), "Input is the wrong form"
    assert obj_normalized >= 1, "no objects were created"
    assert black + obj_normalized*25 == 62500, "the total pixel number is not correct"
    return black, obj_normalized


#Function 9: Test of pixel counter for all images of rectangles
def test_pix_count_array_rect():
    """Test: Counts the number of rectangles in the images array"""
    #function Inputs
    n = 2
    array = training_images.im_gen_rect(n)
    #function performance
    pixel_count = training_images.pix_count_array_rect(array)
    #checks and asserts
    assert isinstance(n, int), "input is the wrong form"
    assert isinstance(array, list), "input is in the wrong form"
    return pixel_count

#Function 10: Test of image rectangle generator
def test_im_gen_circles_and_rect():
    """Test: Generates images with random rectangles and circles"""
    #function Inputs
    n = 2
    #function performance
    imgarray = training_images.im_gen_circles_and_rect(n)
    #checks and asserts
    assert isinstance(n, int), "input is the wrong form"
    assert isinstance(imgarray, list), "output is in the wrong form"
    return imgarray
