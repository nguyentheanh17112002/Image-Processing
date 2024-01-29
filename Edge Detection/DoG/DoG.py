import cv2

if __name__ == "__main__":
    im = cv2.imread("002.jpg", cv2.IMREAD_GRAYSCALE)
    im = cv2.equalizeHist(im)

    low_sigma = cv2.GaussianBlur(im, (45, 45), 0)
    high_sigma  = cv2.GaussianBlur(im, (49, 49), 0)

    dog = low_sigma - high_sigma

    cv2.imwrite("DoG_002.jpg", dog)