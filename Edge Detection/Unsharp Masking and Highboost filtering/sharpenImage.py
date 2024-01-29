import cv2

if __name__ == "__main__":
    im = cv2.imread("002.jpg")

    gauss = cv2.GaussianBlur(im, (3,3), 0)
    gamma = 0
    out = cv2.addWeighted(im, 2, gauss, -1, gamma)

    cv2.imwrite("sharpen_002.jpg", out)