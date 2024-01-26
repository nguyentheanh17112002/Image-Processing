import cv2

if __name__ == "__main__":

    # Read an image
    img = cv2.imread('image.jpg')
    rows,cols,_ = img.shape
    
    # Create the transformation matrix
    M = cv2.getRotationMatrix2D(((cols-1)/2.0,(rows-1)/2.0),90,1)
    
    # Pass it to warpAffine function
    dst = cv2.warpAffine(img,M,(cols,rows))
    
    cv2.imwrite("cv2.jpg", dst)