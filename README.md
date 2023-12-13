Dibuat oleh: 
Nama: Edinta Bahagia
Nim: 120140235


Pada bagian:
def main():
    # Load the image
    image = cv2.imread("CM_matang1.jpg") -> pada bagian ini diganti sesuai dengan nama file yang ingin dibaca

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Canny edge detection
    edges_canny = canny
