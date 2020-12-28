"""
    This script is a benchmark to test different FIR filter on real time implementation (sample by sample)
    Author. Gabriel Galeote Checa
    email: gabriel@imse-cnm.csic.es
    GNU license
"""
import matplotlib.pylab as plt
import numpy as np
from scipy import signal
import fir

fs = 2000  # Hertz
NTAPS = 1000
SAMPLES = 100 * fs

unfiltered = np.loadtxt('unfiltered.dat')
input = unfiltered[:,1]
mysignal = input[:SAMPLES]
plt.figure(1)
plt.plot(mysignal)

f1 = 1
f2 = 40
b = signal.firwin(NTAPS,[f1/(fs*2) ,f2/(fs*2)], pass_zero = 'bandpass', fs = fs)

myFIR = fir.FIR_filter(b, NTAPS)
y = np.zeros(SAMPLES)
for i in range(SAMPLES):
    y[i] = myFIR.dofilter(mysignal[i])

plt.figure(2)
plt.subplot(211)
plt.plot(mysignal)
plt.subplot(212)
plt.plot(y)

unfilteredfft = np.fft.fft(mysignal)
filteredfft = np.fft.fft(y)

f = np.linspace(0, fs, SAMPLES)

plt.figure(3)
plt.subplot(211)
plt.loglog(f[:SAMPLES // 2], np.abs(unfilteredfft)[:SAMPLES // 2] * 1 / SAMPLES)
plt.subplot(212)
plt.loglog(f[:SAMPLES // 2], np.abs(filteredfft)[:SAMPLES // 2] * 1 / SAMPLES)

np.savetxt('coefficients.dat', b, fmt='%f', delimiter='')

plt.show()

