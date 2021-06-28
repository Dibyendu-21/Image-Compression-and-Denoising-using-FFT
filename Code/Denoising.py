# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 11:51:01 2021

@author: Sonu
"""

from fourier_lib import low_pass_filter, display_results
import cv2 
import numpy as np

""" Denoising the image.
    The goal is to remove the noise from the provided images (in resources/) by applying a lowpass filter.
    that removes the frequencies above a cutoff frequency. 
"""
def noise():
    for i in range(1, 2):
        filename = "./Noisy_Image.png"
        original = cv2.imread(filename, 0)

        #Finding the fast fourier transform of the image. 
        spectrum = np.fft.fft2(original) 
        thresh_val = 0.08
        
        #Keeping only the low frequency components of the spectrum by appying a low pass filter
        spectrum_filtered = low_pass_filter(spectrum, thresh_val)
        
        #Retransforming the spectrum from frequency domain to time domain
        filtered = np.fft.ifft2(spectrum_filtered) 
        
        #Fourier Represenation of any signal consists of both real and imagonary parts.
        #Keeping only the real part of the transformed image and removing the imaginary part.
        filtered = np.real(filtered)

        display_results(spectrum, spectrum_filtered, original, filtered)

noise()