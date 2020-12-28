
Realtime FIR filter implementation and benchmark in Python

=======================================


This is a project where you can create, test, evaluate FIR filters. Besides, an FIR filter class is provided to perform realtime
processing of a signal. It was designed to achieve efficiency by using only simple operations. 

Benchmark
=========

Here, an implementation of a simple FIR filter using python is provided. First, you might need to create and custom your own FIR filter by using firwin functions or other methods.  

Import the filter
======

Use this command to import it:

  import fir

Calculate the coefficients
==========================

You can extract yout filter coefficients from the FIR filter design benchmark and design file:

    b = signal.firwin(NTAPS,[f1/(fs*2) ,f2/(fs*2)], pass_zero = 'bandpass', fs = fs)

Instantiate the filter
==================

You can create an instance of the FIR filter by calling it:

    myFIR = fir.FIR_filter(b, NTAPS)

Filtering Flow
====

In the realtime script, a combination of sine waves can be created from the function provided. In the case of the example provided, a combination of a 1 and 50 Hz sine waves are provided.

For filtering sample by sample:
````
  y = np.zeros(SAMPLES)
    for i in range(SAMPLES):
       y[i] = myFIR.dofilter(mysignal[i])
````

And you obtain something like this:

![Figure_2](https://user-images.githubusercontent.com/16301652/101928475-ee7a5700-3bd5-11eb-9cdb-1f15a0c49a4d.png)
