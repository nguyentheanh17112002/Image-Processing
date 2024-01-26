import cv2
import numpy as np

if __name__ == "__main__":
    im = cv2.imread("flower.jpg")

    rows, cols, _ = im.shape
    src = np.float32([[0,0], [cols - 1, 0], [0, rows - 1]])
    dst = np.float32([[cols + 19, 20], [20,20], [cols + 19, rows + 19]])

    M = cv2.getAffineTransform(src, dst)

    new_img = cv2.warpAffine(im, M, (cols + 100, rows + 100))

    cv2.imwrite("new.jpg", new_img)