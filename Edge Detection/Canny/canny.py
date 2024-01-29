import cv2
import numpy as np

def enhance_edges(image):
    # Chuyển đổi ảnh sang ảnh grayscale (nếu chưa là ảnh grayscale)
    gray = image

    # Áp dụng bộ lọc Sobel để tính đạo hàm theo hướng x và y
    sobel_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
    sobel_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)

    # Tính toán độ lớn đạo hàm
    magnitude = np.sqrt(sobel_x**2 + sobel_y**2)

    # Chuẩn hóa độ lớn đạo hàm về khoảng [0, 255]
    magnitude = np.uint8(magnitude)

    return magnitude

if __name__ == "__main__":
    img = cv2.imread("002.jpg", cv2.IMREAD_GRAYSCALE)
    # cv2.imwrite("gray_002.jpg", img)

    img = enhance_edges(img)
    # cv2.imwrite("hist_002.jpg", img)

    blurred = cv2.GaussianBlur(img, (3, 3), 0)
    sigma = 0.33
    v = np.mean(blurred)
    # apply automatic Canny edge detection using the computed median
    lower = int(max(0, (1.0 - sigma) * v))
    upper = int(min(255, (1.0 + sigma) * v))
    # Áp dụng Canny với ngưỡng gradient trung bình
    edges = cv2.Canny(blurred, lower, upper)

    cv2.imwrite("Mask_002.jpg", edges)
