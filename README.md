
Realtime FIR filter implementation in Python
=======================================

This project is a simple FIR filter implementation in python to process signals in a realtime mode, sample by sample. The FIR filter is implemented in a python class that can be used in any of your python projects. 

Import the filter
======

Use this command to import the fir class in your python script.
````
  import fir
````
Calculate the coefficients
==========================

You can extract yout filter coefficients from the FIR filter design benchmark and design file:
````
    b = signal.firwin(NTAPS,[f1/(fs*2) ,f2/(fs*2)], pass_zero = 'bandpass', fs = fs)
````
In the design process, implementation requirements must be taken in accordance to which behaviour is required on your application. Here is where your expertise and knowledge about DSP come into play. I can provide some recommended literature to understand the world of digital signal processing:
1. http://www.dspguide.com/
2. Discrete-Time Signal Processing by A. V. Oppenheim and R. W. Schafer.
3. Theory and Application of Digital Signal Processing by Rabiner and Gold. 

Instantiate the filter
==================

You can create an instance of the FIR filter by calling it:
````
    myFIR = fir.FIR_filter(b, NTAPS)
````

Filtering Flow
====

In the script, a combination of sine waves can be created from the function provided. In the case of the example provided, a combination of a 1 and 50 Hz sine waves are provided.

For filtering sample by sample:
````
  y = np.zeros(SAMPLES)
    for i in range(SAMPLES):
       y[i] = myFIR.dofilter(mysignal[i])
````

And you obtain something like this:

![signa](https://user-images.githubusercontent.com/16301652/103227026-b4c38300-492d-11eb-99ea-334d0a0a11da.png)

The frequency spectrum of the filtered signal is the following

![fft](https://user-images.githubusercontent.com/16301652/103227030-b55c1980-492d-11eb-8a21-e12f11ff619f.png)
