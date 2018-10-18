import numpy as np

# Using the overlap-add method implements convolving _filter_ (the impulse response in frequency domain)
# As the default DFT length is set to 2048 samples, _filter_ should be an array of length 1025 (the last element corresponds to the nyquist frequency)
# _signal_ is expected to be real 
# The returned signal has the same length as _signal
def overlap_add_filter(signal, filter):
  dft_length = 2048
  segment_length = 1024

  signal_length = signal.shape[0]
  indices = range(0, signal_length, segment_length)

  overlap_results = [np.fft.irfft(np.fft.rfft(testsig[n:n+segment_length], n=dft_length) * filter) for n in indices]
  overlap_add_result = np.zeros(signal_length + dft_length)
  for i, n in enumerate(indices):
      overlap_add_result[n:n+dft_length] += overlap_results[i]
  overlap_add_result = overlap_add_result[:signal_length]
  return overlap_add_result
  
