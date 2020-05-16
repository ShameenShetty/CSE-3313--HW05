# CSE-3313--HW05
This is the coding assignment for Homework 5 for CSE3313 (Introduction to Signal Processing)


## Purpose
Learn how to apply a lowpass filter to music to remove noise with high frequencies.
Also learn how to apply a window to filter coefficients to change the frequency response of
the filter.


### Process
* Read from *P_9_2.wav*, which is a wav file containing a piece of music that has been corrupted with noise.
* We will remove this noise using the lowpass filter from [HW04](https://github.com/ShameenShetty/CSE-3313--HW04/) with the following specifications:  
  - A cut-off freq of f<sub>c</sub> = 7500 Hz
  - Filter len of L = 21, and M = filter len - 1
  
* Instead of using rectangular window, we will apply a Hamming window
* After producing the L Hamming window values, apply them to the filter coefficients by performing an element-wise multiplication between h[n] and w[n].
* We also want to look at the frequency response of our filter before and after applying the window. To do this, we use `x, y = freqz(filter_coefficients, 1)` after importing the library using `from scipy.signal import freqz`.
Note: The y values might be complex, so we will plot them using `plot(x, abs(y))`. We put both the frequency response plots on the ![same figure window.](https://github.com/ShameenShetty/CSE-3313--HW05/blob/master/Frequency%20Response.png)
