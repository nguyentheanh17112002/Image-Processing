import cv2
import numpy as np

def Crop_ROI(img, points):
    rect = np.array(points, dtype=np.float32).reshape(-1,1,2)
    width = 224
    height = 224
    dst = np.array([
        [0, 0],
        [width - 1, 0],
        [width - 1, height - 1],
        [0, height - 1]], dtype="float32").reshape(-1,1,2)

    # compute the perspective transform matrix and then apply it
    M = cv2.getPerspectiveTransform(rect, dst)
    crop = cv2.warpPerspective(img, M, (width, height))
    return crop