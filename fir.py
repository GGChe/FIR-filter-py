import numpy as np

"""
FIR_Filter class that applies the FIR filter to an input signal.

This class calculate the result of the FIR filter for a given value. The class function dofilter(input) 
introduces the given value of the signal in the buffer in the current position after a proper management of the 
buffer shifting. Then, it is calculated the mathematical result of FIR filter of the buffer stored that was 
previously shifted to put in the first position the current input value. 
"""
class FIR_filter:
    def __init__(self, inpurFIR, NTAPS):
        self.offset = 0
        self.P = 0
        self.coeval = 0
        self.NTAPS = NTAPS
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

        self.CurrentBufferValue = self.P + self.NTAPS - 1

        while self.coeval < self.NTAPS:
            ResultFIR += self.Buffer[self.CurrentBufferValue] * self.myFIR[self.coeval]
            self.CurrentBufferValue -= 1
            self.coeval += 1

        self.offset += 1

        if self.offset >= self.NTAPS:
            self.offset = 0

        self.coeval = 0
        return ResultFIR




