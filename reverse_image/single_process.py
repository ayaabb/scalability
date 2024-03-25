import cv2


def reverse_pixel(pixel):
    # reverse a pixel
    return [255 - p for p in pixel]

def reverse_image(img_path):
    image = cv2.imread(img_path)
    height, width, _ = image.shape
    for y in range(height):
        for x in range(width):
            image[y][x] = reverse_pixel(image[y][x])

    cv2.imwrite('result_files/reversed_image_single_process.jpg', image)

