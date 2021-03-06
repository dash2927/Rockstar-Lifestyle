#Purpose: To Obtain object stats from the python images

#Import necessary packages
import numpy as np
import scipy
from skimage.feature import peak_local_max
from skimage import measure, morphology, segmentation, data, feature, filters
from scipy import ndimage
import math
import matplotlib.pyplot as plt

#Function 1: Obtaining the Global Threshold binary
def global_binary(image):
    """obtains the binary using the Global Otsu Threshold"""
    image_arr = np.array(image)
    thresh = filters.threshold_otsu(image_arr)
    global_binary = image_arr > thresh
    return global_binary

#Function 2: Obtaining the Local Adaptive Threshold Binary
def local_binary(image, block_size):
    """obtains the binary of the image using a local adaptive threshold"""
    image_arr = np.array(image)
    adaptive_thresh = filters.threshold_local(image_arr,
                                                    block_size, offset=8)
    binary_adaptive = image_arr < adaptive_thresh
    return binary_adaptive

#Function 3: Wrapping function that does all following functions in one step
def global_labels(image):
    """obtains the labels for objects using the global otsu threshold"""
    binary = global_binary(image)
    distance = ndimage.distance_transform_edt(binary)
    local_maxi = peak_local_max(distance, indices=False,
                                footprint=np.ones((3, 3)), labels=binary)
    markers = morphology.label(local_maxi)
    markers[~binary] = -1
    otsu_global_labels = segmentation.random_walker(binary, markers)
    return otsu_global_labels

#Function 4: Performing the Otsu Threshold
def local_labels(image, block_size):
    """obtains the lables using a local adaptive threshold for objects"""
    binary = local_binary(image, block_size)
    distance = ndimage.distance_transform_edt(binary)
    local_maxi = peak_local_max(distance, indices=False,
                            footprint=np.ones((3, 3)), labels=binary)
    markers = morphology.label(local_maxi)
    markers[~binary] = -1
    local_adaptive_labels = segmentation.random_walker(binary, markers)
    return local_adaptive_labels

#Function 5: Creates a binary mask of image
def object_area_hist(properties_local, properties_global):
    """makes 10-bin histograms of the object areas"""
    areas_local_adaptive = [prop.bbox_area for prop in properties_local]
    areas_global = [prop.bbox_area for prop in properties_global]
    fig = plt.figure()
    ax1 = plt.subplot(211)
    ax2 = plt.subplot(212)

    ax1.hist(areas_global, bins=10, density = True, cumulative = False)
    ax1.set_title('Global Otsu Threshold')
    ax1.set_ylabel('Frequency')
    ax1.set_xlabel('Object Area')

    ax2.hist(areas_local_adaptive, bins=10, density = True, cumulative = False)
    ax2.set_title('Local Threshold')
    ax2.set_ylabel('Frequency')
    ax2.set_xlabel('Object Area')

    fig.tight_layout()
    return

#Function 6: finds the distance between an object and image centroid
def centroid_distance(image_centroid, object_centroid, row):
    """computes distance between an object centroid and image centroid"""
    X1 = image_centroid[0]
    Y1 = image_centroid[1]
    X2 = object_centroid[row][0]
    Y2 = object_centroid[row][1]
    distance = math.sqrt((X1-X2)**2+(Y1-Y2)**2)
    return distance

#Function 7: Calculates distances from centroid to image
def distancesarr(image_centroid, object_centroids):
    """gets the distances between image and objects"""
    distances = []
    j = 0
    for row in object_centroids:
        distance = centroid_distance(image_centroid, object_centroids, j)
        distances.append(distance)
        j +=1
    return distances

#Function 8: Finds object centroids
def objectcentroids(image, block_size):
    """obtaining the object centroids"""
    global_binarys = global_binary(image)
    object_centroids = feature.blob_log(global_binarys)
    local_binarys = local_binary(image, block_size)
    object_centroids_local = feature.blob_log(local_binarys)
    return object_centroids, object_centroids_local

#Function 9: Creates a 10-bin histgoram of object to image centroids
def distance_histograms(image, block_size):
    """obtaining 10-bin histograms of centroid distances"""
    otsu_global_labels = global_labels(image)
    local_adaptive_labels = local_labels(image, block_size)
    properties_global = measure.regionprops(otsu_global_labels)
    properties_local = measure.regionprops(local_adaptive_labels)
    image_centroid = properties_global[0].centroid
    image_centroid_adaptive = properties_local[0].centroid
    object_centroids, object_centroids_local = objectcentroids(image, block_size)
    distances_global = distancesarr(image_centroid, object_centroids)
    distances_local = distancesarr(image_centroid_adaptive, object_centroids_local)
    fig = plt.figure()
    ax1 = plt.subplot(211)
    ax2 = plt.subplot(212)
    ax1.hist(distances_global, bins=10, density = True, cumulative = False)
    ax1.set_title('Global Otsu Threshold')
    ax1.set_ylabel('Frequency')
    ax1.set_xlabel('Pixel Distance')
    ax2.hist(distances_local, bins=10, density = True, cumulative = False)
    ax2.set_title('Local Threshold')
    ax2.set_ylabel('Frequency')
    ax2.set_xlabel('Pixel Distance')
    fig.tight_layout()
    return

#Function 10: Counts the number of objects in a labeled image
def objectnumber(image, block_size):
    """Gets the object number for the global and local thresholds"""
    global_binarys = global_binary(image)
    object_centroids = feature.blob_log(global_binarys)

    local_binarys = local_binary(image, block_size)
    object_centroids_local = feature.blob_log(local_binarys)

    object_number_global = len(object_centroids)
    print('Gobal Threshold Object Number:     ', object_number_global)

    object_number_local = len(object_centroids_local)
    print('Local Threshold Object Number:    ', object_number_local)
    return

#Function 11: Gets basic stats and prints them of an object property
def stats(property):
    """gets basic stats for whatever property input"""
    mins= min(property)
    maxs= max(property)
    means= np.mean(property)
    medians= np.median(property)
    variances= np.var(property)

    print('Minimum:     ', mins)
    print('Maximum:     ', maxs)
    print('Mean:     ', means)
    print('Median:     ', medians)
    print('Variance:     ', variances)
    return
