import cv2

if __name__ ==  "__main__":
    img = cv2.imread("original.jpeg", cv2.IMREAD_GRAYSCALE)

    hist_img = cv2.equalizeHist(img)

    cv2.imwrite("hist.jpg", hist_img)