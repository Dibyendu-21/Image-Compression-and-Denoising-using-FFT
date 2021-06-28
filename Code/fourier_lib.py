# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 11:38:54 2021

@author: Sonu
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm

#Returns distances from the DC component or zero-frequency component
def get_dist_from_center_matrix(spectrum):
    rows, cols = spectrum.shape
    print('No of rows:',rows, 'No of columns:',cols)
    
    #Finding the center of spectrum
    r_center = rows // 2
    c_center = cols // 2
    
    #Calculating the distance of pixel from the center of spectrum dx^2 + dy^2
    r = np.power(np.arange(rows) - r_center, 2)
    #Broadcasting the c matrix on r matrix since both are of different dimensions. 
    #Broadcasting requires one of the matrix to be of shape (n,1) hence reshaped.
    c = np.power(np.arange(cols).reshape((cols, 1)) - c_center, 2)
    return r + c


def low_pass_filter(spectrum, thresh):
    #Cutoff frequency = (columns * threshold)^2
    max_distance_sq = (spectrum.shape[1] * thresh)**2
    
    #Shifting the DC component from top-left to center of spectrum
    shifted = np.fft.fftshift(spectrum)

    distance_matrix = get_dist_from_center_matrix(shifted)

    #Create a black or white mask depending on whether the distance from center is greater than threshold 
    circle_mask = np.where(distance_matrix > max_distance_sq, 0, 1)
    
    #Applying the mask created on the shifted spectrum
    filtered = shifted * circle_mask.T

    #Shifting the DC component back to top-left portion of spectrum
    return np.fft.ifftshift(filtered)


def plot_spectrum(spectrum):
    #Plots the Fourier space (spectrum), by taking the amplitudes of the Fourier Coefficients
    plt.imshow(np.abs(spectrum), norm=LogNorm(vmin=5))
    plt.colorbar()

 
#DisplayING the result for the two exercices denoising and compression
def display_results(spectrum, filtered_spectrum, original, filtered):
    plt.figure()
    plt.subplot(221)
    plot_spectrum(spectrum)

    plt.subplot(222)
    plot_spectrum(filtered_spectrum)

    plt.subplot(223)
    plt.axis('off')
    plt.imshow(original, cmap='gray')

    plt.subplot(224)
    plt.axis('off')
    plt.imshow(filtered, cmap='gray')

    plt.show()
