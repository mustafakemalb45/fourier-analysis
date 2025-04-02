import numpy as np
import soundfile as sf
from scipy.fftpack import fft
import matplotlib.pyplot as plt

# Ses dosyasının tam yolu
file_path = "C:/Users/Mustafa K. Ballıöz/Documents/Ses Kayıtları/Fizik.wav"

# Ses dosyasını yükle
data, samplerate = sf.read(file_path)

# Stereo dosya olup olmadığını kontrol et ve mono'ya çevir
if len(data.shape) > 1:
    data = np.mean(data, axis=1)

# Fourier dönüşümünü uygula
fourier = fft(data)

# Frekans ekseni oluştur
frekans = np.fft.fftfreq(len(fourier), 1/samplerate)

# Sadece pozitif frekansları al
mask = frekans >= 0
fourier = fourier[mask]
frekans = frekans[mask]

# Grafik çiz
plt.plot(frekans, np.abs(fourier))
plt.xlabel('Frekans (Hz)')
plt.ylabel('Genlik')
plt.title('Ses Dosyasının Fourier Dönüşümü')
plt.show()

