import cv2
import matplotlib.pyplot as plt
import numpy as np

# Baca gambar cabai
# Ganti 'nama_file_gambar.jpg' dengan nama file gambar cabai Anda
img = cv2.imread('Cabaisegar.jpg')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # Ubah ke citra keabuan

# Deteksi tepi menggunakan operator Roberts
edges_roberts = cv2.filter2D(img_gray, -1,
                             np.array([[1, 0], [0, -1]]),
                             borderType=cv2.BORDER_REFLECT)

# Tampilkan gambar asli dan hasil deteksi tepi Roberts
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title('Gambar Asli')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(edges_roberts, cmap='gray')
plt.title('Deteksi Tepi Roberts')
plt.axis('off')

plt.tight_layout()
plt.show()
