import matplotlib.pylab as plt
import numpy as np
from scipy import signal

# Variable declaration
SAMPLE_RATE = 2000  # Hertz
DURATION = 5  # Seconds
NTAPS = 1000
SAMPLES = DURATION * SAMPLE_RATE

f1 = 0.5
f2 = 45

fig, axs = plt.subplots(2, 2, sharex='col', sharey='row', gridspec_kw={'hspace': 0, 'wspace': 0})
(ax1, ax2), (ax3, ax4) = axs
fig.suptitle('Magnitude response of a bandpass filter with blackman, hamming, triang, blackmanharris windows')
# Butter Bandpass window blackman
b1 =signal.firwin(NTAPS, [f1, f2], pass_zero=False, window='blackman', width=5, fs = SAMPLE_RATE)
ax1.plot(b1)

# Butter Bandpass hamming window
b2 =signal.firwin(NTAPS, [f1, f2], pass_zero=False, window='hamming', fs = SAMPLE_RATE)
ax2.plot(b2, 'tab:orange')

# Butter Bandpass triang window
b3 =signal.firwin(NTAPS, [f1, f2], pass_zero=False, window='triang', fs = SAMPLE_RATE)
ax3.plot(b3, 'tab:green')

b4 =signal.firwin(NTAPS, [f1, f2], pass_zero=False, window='blackmanharris', fs = SAMPLE_RATE)
ax4.plot(b4, 'tab:red')

plt.show()












