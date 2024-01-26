import cv2
import numpy as np

def change_intensity(img, a, b):
    img = np.asarray(a*img + b, dtype=int)
    
    img[img > 255] = 255
    img[img < 0] = 0

    
    return img

if __name__ == "__main__":
    img = cv2.imread("/home/anhnt596/Work Space/Image Processing/image.jpg")

    new_img = change_intensity(img, 0.5, 10)

    cv2.imwrite("Change2.jpg", new_img)
