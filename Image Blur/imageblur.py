import cv2

if __name__ == "__main__":
    img = cv2.imread("original.jpg")

    gaussian = cv2.GaussianBlur(img,(7,7), 0)
    cv2.imwrite("gaussian.jpg", gaussian)

    median = cv2.medianBlur(img, 5)
    cv2.imwrite("median.jpg", median)

    bilateral = cv2.bilateralFilter(img, 9, 75, 75)
    cv2.imwrite("bilateral.jpg", bilateral)