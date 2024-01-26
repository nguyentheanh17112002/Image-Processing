import cv2

if __name__ == "__main__":
    original = cv2.imread("original.png")

    original = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)

    _, thresh1 = cv2.threshold(original,120, 255, cv2.THRESH_BINARY)
    _, thresh2 = cv2.threshold(original,120, 255, cv2.THRESH_BINARY_INV)    
    _, thresh3 = cv2.threshold(original,120, 255, cv2.THRESH_TRUNC)
    _, thresh4 = cv2.threshold(original,120, 255, cv2.THRESH_TOZERO)
    _, thresh5 = cv2.threshold(original,120, 255, cv2.THRESH_TOZERO_INV)

    cv2.imwrite("Gray.jpg", original)
    cv2.imwrite("ThreshBinary.jpg", thresh1)
    cv2.imwrite("ThreshBinaryInv.jpg", thresh2)
    cv2.imwrite("Trunc.jpg", thresh3)
    cv2.imwrite("ToZero.jpg", thresh4)
    cv2.imwrite("ToZeroInv.jpg", thresh5)