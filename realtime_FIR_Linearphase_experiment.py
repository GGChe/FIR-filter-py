"""
    This script is a benchmark to test different FIR filter on real time implementation (sample by sample)
    Author. Gabriel Galeote Checa
    email: gabriel@imse-cnm.csic.es
    GNU license
"""
import matplotlib.pylab as plt
import numpy as np
from scipy import signal
from scipy.signal import minimum_phase, freqz, group_delay

SAMPLE_RATE = 2000  # Hertz
NTAPS = 1000
SAMPLES = 100 * SAMPLE_RATE

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

unfiltered = np.loadtxt('unfiltered.dat');
input = unfiltered[:,1] 
mysignal = input[:SAMPLES]  

f2 = 40
b = signal.firwin(NTAPS, f2/(SAMPLE_RATE*2), pass_zero = True)
myFIR = FIR_filter(b)


impulse = np.zeros(1000)
impulse[10] = 1
impulseresponse = np.zeros(1000) 
print("-- Start computation of impulse response --")

plt.figure(1)
for i in range(1000):
    impulseresponse[i] = myFIR.dofilter(impulse[i])

plt.subplot(311)
plt.plot(impulseresponse)

h_min_hom = minimum_phase(b, method='homomorphic')
h_min_hil = minimum_phase(b, method='hilbert')

myFIR1 = FIR_filter(h_min_hom)
myFIR2 = FIR_filter(h_min_hil)

NTAPS = 500 # Because the linearization removes half of the spectrum to reduce group delay  

for i in range(1000):
    impulseresponse[i] = myFIR1.dofilter(impulse[i])

plt.subplot(312)
plt.plot(impulseresponse)

for i in range(1000):
    impulseresponse[i] = myFIR2.dofilter(impulse[i])

plt.subplot(313)
plt.plot(impulseresponse)

print("-- Start computation of filteringS --")

plt.figure(2)
NTAPS = 1000

plt.subplot(411)
plt.plot(mysignal)
plt.xlim((20000,60000))

y1 = np.zeros(SAMPLES)
y2 = np.zeros(SAMPLES)
y3 = np.zeros(SAMPLES)

for i in range(SAMPLES):
    y1[i] = myFIR.dofilter(mysignal[i])

plt.subplot(412)
plt.plot(y1)
plt.xlim((20000,60000))

NTAPS = 500

for i in range(SAMPLES):
    y2[i] = myFIR1.dofilter(mysignal[i])

plt.subplot(413)
plt.plot(y2)
plt.xlim((20000,60000))

for i in range(SAMPLES):
    y3[i] = myFIR2.dofilter(mysignal[i])

plt.subplot(414)
plt.plot(y3)
plt.xlim((20000,60000))

print("-- Finished calculations --")
print("-- Start Frequency spectrum calculations --")

plt.figure(3)
plt.subplot(211)
plt.plot(mysignal)

plt.subplot(212)
plt.plot(y1)

unfilteredfft = np.fft.fft(mysignal)
filteredfft1 = np.fft.fft(y1)
filteredfft2 = np.fft.fft(y2)
filteredfft3 = np.fft.fft(y3)

f = np.linspace(0, SAMPLE_RATE, SAMPLES)

plt.figure(4)
plt.subplot(411)
plt.loglog(f[:SAMPLES // 2], np.abs(unfilteredfft)[:SAMPLES // 2] * 1 / SAMPLES)  # 1 / N is a normalization factor
plt.subplot(412)
plt.loglog(f[:SAMPLES // 2], np.abs(filteredfft1)[:SAMPLES // 2] * 1 / SAMPLES)  # 1 / N is a normalization factor
plt.subplot(413)
plt.loglog(f[:SAMPLES // 2], np.abs(filteredfft2)[:SAMPLES // 2] * 1 / SAMPLES)  # 1 / N is a normalization factor
plt.subplot(414)
plt.loglog(f[:SAMPLES // 2], np.abs(filteredfft3)[:SAMPLES // 2] * 1 / SAMPLES)  # 1 / N is a normalization factor
plt.show()


np.savetxt('coefficients_fir.dat', b, fmt='%f', delimiter='')
np.savetxt('coefficients_fir_norm_homomorphic.dat', h_min_hom, fmt='%f', delimiter='')
np.savetxt('coefficients_fir_norm_hilbert.dat', h_min_hil, fmt='%f', delimiter='')

print("Done!")
