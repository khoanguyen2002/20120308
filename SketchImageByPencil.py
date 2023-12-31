import cv2

imagePath = 'Shiba.jpg'
image = cv2.imread(imagePath)

if image is None :
    print("Unvalid path ")

else  :
    grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    inverted = 255 - grayImage

    blur = cv2.GaussianBlur(inverted, (21, 21), 0)

    invertedBlur = 255 - blur

    sketch = cv2.divide(grayImage, invertedBlur, scale=242.0)

    cv2.imwrite("SketchImage.jpg", sketch)

    cv2.imshow("Sketch Image", sketch)

    cv2.waitKey(0)
    cv2.destroyAllWindows()