import numpy as np
import matplotlib.pyplot as plt

# Elde ettiğiniz a_n ve b_n katsayıları
a_n = np.array([4.46422855, -0.80424965, -1.10423126, 4.26739798, -1.74494258, -0.3071958])  # Örnek değerler
b_n = np.array([0.0, -0.93365868, 1.55311407, 0.0323875, 0.78616597, 1.78824636])  # Örnek değerler

# Frekanslar (n değerleri)
n_values = np.arange(len(a_n))

# Grafik çizimi
plt.figure(figsize=(12, 6))

# a_n katsayıları grafiği
plt.subplot(2, 1, 1)
plt.stem(n_values, a_n)  # use_line_collection kaldırıldı
plt.title('Fourier Katsayıları a_n')
plt.xlabel('n')
plt.ylabel('a_n Katsayıları')
plt.grid()

# b_n katsayıları grafiği
plt.subplot(2, 1, 2)
plt.stem(n_values, b_n)  # use_line_collection kaldırıldı
plt.title('Fourier Katsayıları b_n')
plt.xlabel('n')
plt.ylabel('b_n Katsayıları')
plt.grid()

plt.tight_layout()
plt.show()
