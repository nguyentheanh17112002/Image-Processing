import cv2

if __name__ == "__main__":
    img = cv2.imread("002.jpg", cv2.IMREAD_GRAYSCALE)

    thresh2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
                                          cv2.THRESH_BINARY, 195, 5)

    cv2.imwrite("otsu.jpg", thresh2)