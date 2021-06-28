# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 11:41:36 2021

@author: Sonu
"""

from fourier_lib import low_pass_filter, display_results
import cv2 
import numpy as np

#Mapping the real components of the image to the 8-bit number space
def real_to_int(image):
    image = (image - image.min()) * 255 / (image.max() - image.min())
    return np.uint8(image)

""" 
    Compressing the image.
    The goal is to compress an image using the Fourier Transform by manipulating the resulting Fourier Space 
    by removing the frequencies above a cutoff frequency that the human eye might not perceive.
"""

def compression(deg):
    #Degrees of compression, ranging from 0 to 9, 0 being not compressed at all and 9 "relatively" compressed to max. 
    assert deg in range(0,10)

    file_2_read = "./Noisy_Image.png"
    file_2_write = "./compressed.png"

    original = cv2.imread(file_2_read, 0)
    cv2.imshow("Original Image", original)
    cv2.waitKey(10000)
    cv2.destroyAllWindows()

    original = np.double(original)
    #Finding the fast fourier transform of the image. 
    spectrum = np.fft.fft2(original)
    thresh = 1.0 - (deg / 10.0)
    
    #Compressing the image by keeping only the low frequency components of the spectrum by appying a low pass filter
    compressed_spectrum = low_pass_filter(spectrum, thresh)
    
    #Retransforming the spectrum from frequency domain to time domain
    compressed_image = np.fft.ifft2(compressed_spectrum) 
    
    #Coverting the real part of the transformed spectrum to 8-bit number space.
    compressed_image = real_to_int(compressed_image.real)
 
    cv2.imwrite(file_2_write, compressed_image)

    display_results(spectrum, compressed_spectrum, original, compressed_image)

compression(deg = 9)