"""
Name: Shameen Shetty
ID:   1001429743
"""

import numpy as np
from scipy.signal import freqz
import soundfile as sf
import matplotlib.pyplot as plt

if __name__ == "__main__":
    
    # Reading from the .wav file and getting the data and sampleRate
    data, sampleRate = sf.read('P_9_2.wav')
    
    f_c = 7500 #Cutoff freq is 7500Hz
    filterLen = 101 #Filter Length of 101
    M = filterLen - 1
    
    f_t = f_c / sampleRate #getting the Normalized transistion freq
    
    """
    For the below for loop we are setting up a low pass filter of len filterLen
    """
    lowPassFilter = []
    hammingWindow = []
    for n in range(filterLen):
        if (n != M/2):
            numerator = np.sin(2* np.pi * f_t * (n - (M/2)))
            denominator = np.pi * (n - (M/2))
            
            lowPassFilter.append(numerator / denominator)
        if (n == M/2):
            lowPassFilter.append(2 * f_t)
        
        theta = (2 * np.pi * n) / M
        hammingWeight = 0.54 - (0.46 * np.cos(theta))
        
        hammingWindow.append(hammingWeight)
            
    #We are convolving the data with the lowPassFilter to remove noise
    convolvedData = np.convolve(data, lowPassFilter)
    """
    Finally we use the convolvedData along with the original sampleRate and the
    function sf.write to output a .wav file 
    """
    sf.write('cleanMusic.wav', convolvedData, sampleRate)
    
    """doing elementwise multiplication between hammingWindow values and the
    lowPassfilter coefficients"""
    windowed = np.multiply(hammingWindow, lowPassFilter)

    original_x, original_y = freqz(lowPassFilter, 1)
    windowed_x, windowed_y = freqz(windowed, 1)
    
    fig, axs = plt.subplots(1)
    plt.plot(original_x, abs(original_y))
    plt.plot(windowed_x, abs(windowed_y))
    axs.legend(loc='upper right', labels=['original', 'windowed'])
    plt.title("Frequency Response")
    fig.tight_layout()
    plt.show()
