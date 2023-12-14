import cv2

# Membaca citra cabai
image = cv2.imread('Cabaisegar.jpg')

# Konversi citra ke citra grayscale
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Tentukan ukuran kernel median filter
kernel_size = 5

# Terapkan median filter pada citra cabai
image_filtered = cv2.medianBlur(image_gray, kernel_size)

# Tampilkan citra cabai asli dan citra cabai yang telah difilter
cv2.imshow('Citra Cabai Asli', image)
cv2.imshow('Citra Cabai yang Telah difilter', image_filtered)
cv2.waitKey(0)
