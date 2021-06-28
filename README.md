# Image Compression and Denoising using FFT
This repo gives information about the decompression and denoising of a noisy image using FFT. 

## Image Compression: 
The goal of compression is to compress an image using the Fourier Transform by manipulating the resulting Fourier Space by removing the frequencies above a cutoff frequency that the human eye might not perceive. 

### Design Pipeline
The Design pipeline of compression is as follows:
* Specify the degree of compression, ranging from 0 to 9, 0 being not compressed at all and 9 "relatively" compressed to max. 
* Read the noisy image.
* Find the fast fourier transform of the image using FFT. 
* Compressing the image by keeping only the low frequency components of the spectrum by appying a low pass filter as follows:
  - Specify cutoff-frequency as: (columns * threshold)^2
  - Shift the DC component from top-left to center of spectrum using fourier shift.
  - Find the center of the spectrum which is the DC component or zero frequency component.
  - Get the distance of each pixel from the DC component.
  - Create a black or white mask depending on whether the distance from center is greater than threshold or not.
  - Apply the mask created on the shifted spectrum.
  - Shift the DC component back to top-left portion of spectrum using inverse fourier shift.
* Retransform the spectrum from frequency domain to time domain using inverse fourier transform.
* Covert the real part of the transformed spectrum to 8-bit number space.
* Display the compressed image.

## Denoising: 
The goal of denoising is to remove the noise from the provided images by applying a lowpass filter that removes the frequencies above a cutoff frequency. 

### Design Pipeline
The Design pipeline of denoising is as follows:
* Read the noisy image.
* Find the fast fourier transform of the image using FFT. 
* Compressing the image by keeping only the low frequency components of the spectrum by appying a low pass filter as follows:
  - Specify cutoff-frequency as: (columns * threshold)^2
  - Shift the DC component from top-left to center of spectrum using fourier shift.
  - Find the center of the spectrum which is the DC component or zero frequency component.
  - Get the distance of each pixel from the DC component.
  - Create a black or white mask depending on whether the distance from center is greater than threshold or not.
  - Apply the mask created on the shifted spectrum.
  - Shift the DC component back to top-left portion of spectrum using inverse fourier shift.
* Retransform the spectrum from frequency domain to time domain using inverse fourier transform.
* Keep only the real part of the transformed image and removing the imaginary part.

