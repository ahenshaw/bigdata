num_samples = 100

# set seed value (optional)
np.random.seed(10)

# generate numpy array of random numbers
#this are the x(n) values 
x = np.random.rand(num_samples)-0.5

# filter order
L = 4
h = np.ones(L)/L

plt.figure(11)
plt.stem(h)
plt.xlim([-1,4])
plt.title('Impulse Response - Coefficients of Simple Averager Filter')
N_fft = 1024 #use a power of two

# frequency response
# the second argument of fft is the number of fft bins to use.
freq_response = np.fft.fft(h,N_fft)

# Transform using DFT to get the frequency response
freq = np.fft.fftfreq(freq_response.size)


# plot filter frequency response
plt.figure(1)
plt.plot(freq, abs(freq_response), 'b.');
plt.ylabel('Amplitude', color='b');
plt.xlabel('Frequency');
plt.grid(True);
plt.title('Frequency Response of Simple Averager Filter');


# plot input frequency spectrum by
# using the FFT to convert time to frequency
x_spectrum = np.fft.fft(x,N_fft)

plt.figure(2)
plt.plot(freq, abs(x_spectrum), 'b.', label='Input');
plt.ylabel('Amplitude', color='b');
plt.xlabel('Frequency');
plt.grid(True);
plt.title('Input Signal Frequency Spectrum');

# Plot output spectrum
y = np.convolve(h,x)

#the following two lines provide the same thing
#1) output spectrum by convolution in the time domain and 
#using FFT to convert to frequency domain

y_spectrum_convolve = np.fft.fft(y,N_fft)

#2) output spectrum by multiplying in the frequency domain

y_spectrum_multiply = abs(x_spectrum)*freq_response

#plt.plot(freq, abs(y_spectrum), 'r.', label='Output');
plt.plot(freq, abs(y_spectrum_convolve), 'r', label = 'Output')
plt.ylabel('Amplitude');
plt.xlabel('Frequency');
plt.grid(True);
plt.title('Signal Spectrum After Filtering (Red)');
plt.legend();
