import cv2
import matplotlib.pyplot as plt

# Baca gambar cabai
# Ganti 'nama_file_gambar.jpg' dengan nama file gambar cabai Anda
img = cv2.imread('Cabaisegar.jpg')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # Ubah ke citra keabuan

# Deteksi tepi menggunakan operator Prewitt
edges_prewitt_x = cv2.Sobel(img_gray, cv2.CV_64F, 1, 0, ksize=3)
edges_prewitt_y = cv2.Sobel(img_gray, cv2.CV_64F, 0, 1, ksize=3)
edges_prewitt = cv2.magnitude(edges_prewitt_x, edges_prewitt_y)

# Tampilkan gambar asli dan hasil deteksi tepi Prewitt
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title('Gambar Asli')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(edges_prewitt, cmap='gray')
plt.title('Deteksi Tepi Prewitt')
plt.axis('off')

plt.tight_layout()
plt.show()
