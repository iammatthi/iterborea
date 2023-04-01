import cv2


def simplify_image(image):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Resize image with max dimension of 500px
    max_dimension = max(image.shape)
    scale = 500 / max_dimension
    image = cv2.resize(image, None, fx=scale, fy=scale)  # type: ignore
    image = cv2.medianBlur(image, 3)

    return image


def invert_image(image):
    return cv2.bitwise_not(image)
