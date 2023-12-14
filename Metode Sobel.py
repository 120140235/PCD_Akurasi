import cv2
import matplotlib.pyplot as plt

# Baca gambar cabai
# Ganti 'nama_file_gambar.jpg' dengan nama file gambar cabai Anda
img = cv2.imread('Cabaisegar.jpg')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # Ubah ke citra keabuan

# Deteksi tepi menggunakan operator Sobel
edges_sobel_x = cv2.Sobel(img_gray, cv2.CV_64F, 1, 0, ksize=3)
edges_sobel_y = cv2.Sobel(img_gray, cv2.CV_64F, 0, 1, ksize=3)
edges_sobel = cv2.magnitude(edges_sobel_x, edges_sobel_y)

# Tampilkan gambar asli dan hasil deteksi tepi Sobel
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title('Gambar Asli')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(edges_sobel, cmap='gray')
plt.title('Deteksi Tepi Sobel')
plt.axis('off')

plt.tight_layout()
plt.show()
