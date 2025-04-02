import pygame

# Ses dosyasının tam yolu
file_path = "C:/Users/Mustafa K. Ballıöz/Documents/Ses Kayıtları/Fizik.wav"


# Pygame'i başlat
pygame.mixer.init()

# Ses dosyasını yükle
pygame.mixer.music.load(file_path)

# Ses dosyasını çal
pygame.mixer.music.play()

# Ses dosyası çalarken bekle
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)
