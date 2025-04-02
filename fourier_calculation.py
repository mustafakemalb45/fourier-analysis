import numpy as np
import soundfile as sf
from scipy.integrate import trapezoid
import matplotlib.pyplot as plt

# Ses dosyasının tam yolu
file_path = "C:/Users/Mustafa K. Ballıöz/Documents/Ses Kayıtları/Fizik.wav"

# Ses dosyasını yükle
try:
    data, samplerate = sf.read(file_path)
    print("Veri Yükleme Başarılı. Örnek Sayısı:", len(data))
    print("Örnekleme Hızı:", samplerate)

    # Eğer veri stereo ise mono'ya dönüştür
    if len(data.shape) > 1:
        data = np.mean(data, axis=1)

    # Pedestal düzeltmesi: sinyalin ortalamasını çıkar
    data_corrected = data - np.mean(data)
    print("Pedestal Düzeltmesi Yapıldı.")

    # Fourier dönüşümünü uygula
    fourier = np.fft.fft(data_corrected)
    frequencies = np.fft.fftfreq(len(fourier), 1/samplerate)

    # Katsayıları hesaplama fonksiyonu
    def calculate_fourier_coefficients(data, frequencies, L, N_limit=500):
        N = len(data)
        a_n = np.zeros(N_limit)
        b_n = np.zeros(N_limit)

        for n in range(N_limit):
            a_n[n] = (2/L) * trapezoid(data * np.cos(2 * np.pi * n * frequencies / L), frequencies)
            b_n[n] = (2/L) * trapezoid(data * np.sin(2 * np.pi * n * frequencies / L), frequencies)
        
        return a_n, b_n

    # Katsayıları hesapla
    L = len(data) / samplerate  # Sinyalin süresi
    print("Katsayılar Hesaplanıyor (ilk 500)...")
    a_n, b_n = calculate_fourier_coefficients(data_corrected, frequencies, L)

    # Sonuçları yazdır
    print("a_n katsayıları (ilk 10):", a_n[:10])
    print("b_n katsayıları (ilk 10):", b_n[:10])

    # Katsayıların grafiğini çiz (use_line_collection kaldırıldı)
    plt.figure(figsize=(10, 5))
    plt.stem(range(10), a_n[:10], label='a_n (Cosine Coefficients)')
    plt.stem(range(10), b_n[:10], markerfmt='C1o', label='b_n (Sine Coefficients)')
    plt.xlabel('n')
    plt.ylabel('Katsayı Değeri')
    plt.title('Fourier Katsayıları')
    plt.legend()
    plt.grid(True)
    plt.show()

except Exception as e:
    print("Hata:", e)
