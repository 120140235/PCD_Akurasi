import cv2


def canny(image):

    # Konversi citra ke citra grayscale
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Penapisan Gaussian
    sigma = 2
    image_filtered = cv2.GaussianBlur(image_gray, (3, 3), sigma)

    # Deteksi tepi
    low_threshold = 0.5
    high_threshold = 0.8
    image_canny = cv2.Canny(image_filtered, low_threshold, high_threshold)

    # Penipisan non-maksimum
    image_canny = cv2.morphologyEx(
        image_canny, cv2.MORPH_CLOSE, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3)))

    return image_canny


# Membaca citra cabai
image = cv2.imread('Cabaisegar.jpg')

# Deteksi tepi Canny
image_canny = canny(image)

# Tampilkan citra cabai asli dan citra tepi Canny
cv2.imshow('Citra Cabai Asli', image)
cv2.imshow('Citra Tepi Canny', image_canny)
cv2.waitKey(0)
