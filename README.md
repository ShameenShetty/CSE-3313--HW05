# CSE-3313--HW05
This is the coding assignment for Homework 5 for CSE3313 (Introduction to Signal Processing)


## Purpose
Learn how to apply a lowpass filter to music to remove noise with high frequencies.
Also learn how to apply a window to filter coefficients to change the frequency response of
the filter.


### Process
* Read from *P_9_2.wav*, which is a wav file containing a piece of music that has been corrupted with noise.
* We will remove this noise using the lowpass filter from [HW04](https://github.com/ShameenShetty/CSE-3313--HW04/) with the following specifications:  
  - A cut-off freq of f<sub>c</sub>= 7500 Hz
