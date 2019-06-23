import playsound
import soundfile as sf
import numpy as np
#import matplotlib.pyplot as plt

x, fs = sf.read('carrie1.wav')
audio = x

#=================================================================================#

fc = 4000
M = 20
wc = (2*np.pi*fc)/fs


#=================================================================================#

w = np.hamming(M)[:M-1]
hd = []
for n in range(M-1):
 hd.insert(n, (wc/np.pi)* np.sinc((wc/np.pi)*(n-(M/2))))

#=================================================================================#

h = hd*w

#=================================================================================#

audio_filtrado = np.convolve(h, audio)


#=================================================================================#

#Espectro do audio Original
#time = np.arange(len(x)) / fs
#plt.plot(time, x)
#plt.xlabel('Tempo(s)')
#plt.ylabel('Amplitude')
#plt.show()
#Espectro do audio_filtrado
#time = np.arange(len(audio_filtrado)) / fs
#plt.plot(time, audio_filtrado)
#plt.xlabel('Tempo(s)')
#plt.ylabel('Amplitude')
#plt.show()

#=================================================================================#

sf.write('musica.wav', audio_filtrado, fs)
