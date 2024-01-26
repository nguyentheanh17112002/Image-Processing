import cv2 

if __name__ == "__main__":
    img = cv2.imread("original.jpg", cv2.IMREAD_GRAYSCALE)

    img_mean = cv2.adaptiveThreshold(img, maxValue=255,adaptiveMethod= cv2.ADAPTIVE_THRESH_MEAN_C,
                                    thresholdType=cv2.THRESH_BINARY,
                                    blockSize= 15,
                                    C = 8 )
    
    img_gauss = cv2.adaptiveThreshold(img, maxValue=255,adaptiveMethod= cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                    thresholdType=cv2.THRESH_BINARY,
                                    blockSize= 15,
                                    C = 8 )
    cv2.imwrite("mean.jpg", img_mean)
    cv2.imwrite("gauss.jpg", img_gauss)