# let's start with the Imports 
import cv2


# Read the image using imread function
image = cv2.imread('image.jpg')
# cv2.imshow('Original Image', image)

# lets downscale the image using new  width and height
width = int(input("Enter image width... "))
height = int(input("Enter image height... "))
points = (width, height)
resized = cv2.resize(image, points, interpolation=cv2.INTER_LINEAR)
# Display images
cv2.imshow('Resized by defining height and width', resized)
cv2.waitKey()
# press any key to close the windows
cv2.destroyAllWindows()
