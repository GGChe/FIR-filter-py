"""
    This script is a benchmark to test different FIR filter on real time implementation (sample by sample)
    Author. Gabriel Galeote Checa
    email: gabriel@imse-cnm.csic.es
    GNU license
"""
import matplotlib.pylab as plt
import numpy as np
from scipy import signal

SAMPLE_RATE = 2000  # Hertz
DURATION = 5  # Seconds
NTAPS = 1000
SAMPLES = DURATION * SAMPLE_RATE

"""
FIR_Filter class that applies the FIR filter to an input signal.

This class calculate the result of the FIR filter for a given value. The class function dofilter(input) 
introduces the given value of the signal in the buffer in the current position after a proper management of the 
buffer shifting. Then, it is calculated the mathematical result of FIR filter of the buffer stored that was 
previously shifted to put in the first position the current input value. 
"""
class FIR_filter:
    def __init__(self, inpurFIR):
        self.offset = 0
        self.P = 0
        self.coeval = 0
        self.Buffer = np.zeros(NTAPS)
        self.myFIR = inpurFIR

    def dofilter(self, v):

        ResultFIR = 0
        self.CurrentBufferValue = self.P + self.offset
        self.Buffer[self.CurrentBufferValue] = v

        while self.CurrentBufferValue >= self.P:
            ResultFIR += self.Buffer[self.CurrentBufferValue] * self.myFIR[self.coeval]
            self.CurrentBufferValue -= 1
            self.coeval += 1

        self.CurrentBufferValue = self.P + NTAPS - 1

        while self.coeval < NTAPS:
            ResultFIR += self.Buffer[self.CurrentBufferValue] * self.myFIR[self.coeval]
            self.CurrentBufferValue -= 1
            self.coeval += 1

        self.offset += 1

        if self.offset >= NTAPS:
            self.offset = 0

        self.coeval = 0
        return ResultFIR

unfiltered = np.loadtxt('sine.dat');
mysignal = unfiltered[:,1] 
plt.figure(1)
plt.plot(mysignal)

f1 = 0.5
f2 = 45
b =signal.firwin(NTAPS, [f1, f2], pass_zero=False, window='blackman', width=5, fs = SAMPLE_RATE)

myFIR = FIR_filter(b)
y = np.zeros(SAMPLES)
for i in range(SAMPLES):
    y[i] = myFIR.dofilter(mysignal[i])

np.savetxt('coefficients.dat', b, fmt='%f', delimiter='')

plt.figure(2)
plt.subplot(211)
plt.plot(mysignal)
plt.subplot(212)
plt.plot(y)

unfilteredfft = np.fft.fft(mysignal)
filteredfft = np.fft.fft(y)

T = 1/SAMPLE_RATE

# 1/T = frequency
f = np.linspace(0, SAMPLE_RATE, SAMPLES)

plt.figure(3)
plt.subplot(211)
plt.plot(f[:SAMPLES // 2], np.abs(unfilteredfft)[:SAMPLES // 2] * 1 / SAMPLES)  # 1 / N is a normalization factor
# plt.plot(20.0*np.log10(unfilteredfft))
plt.subplot(212)
plt.plot(f[:SAMPLES // 2], np.abs(filteredfft)[:SAMPLES // 2] * 1 / SAMPLES)  # 1 / N is a normalization factor

np.savetxt('coefficients.dat', b, fmt='%f', delimiter='')

plt.show()

