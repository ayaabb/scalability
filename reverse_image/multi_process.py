import cv2
import numpy as np
from concurrent.futures import ProcessPoolExecutor


def process_row(row):
    #reverse a row
    return np.array([reverse_pixel(pixel) for pixel in row])


def reverse_pixel(pixel):
    # reverse a pixel
    return [255 - p for p in pixel]


def reverse_image(img_path):
    image = cv2.imread(img_path)
    height, width, _ = image.shape

    # Split the image into rows
    rows = np.array_split(image, height)

    with ProcessPoolExecutor() as executor:
        # Process each row in parallel
        processed_rows = list(executor.map(process_row, rows))

    # Combine processed rows back into the image
    reversed_image = np.vstack(processed_rows)

    # Save the reversed image
    cv2.imwrite('result_files/reversed_image_multiprocess.jpg', reversed_image)
