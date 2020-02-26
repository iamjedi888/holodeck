import os
from typing import List, Tuple, Optional

import cv2


def display_multiple(images: List[Tuple[List, Optional[str]]]):
    """Displays one or more captures in a CV2 window. Useful for debugging

    Args:
        images: List of tuples containing MxNx3 pixel arrays and optional titles OR
            list of image data
    """
    for image in images:
        if isinstance(image, tuple):
            image_data = image[0]
        else:
            image_data = image

        if isinstance(image, tuple) and len(image) > 1:
            title = image[1]
        else:
            title = "Camera Output"

        cv2.namedWindow(title)
        cv2.moveWindow(title, 500, 500)
        cv2.imshow(title, image_data)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def display(pixels, title="Camera Output"):
    """Displays the given capture in a CV2 window. Useful for debugging

    Args:
        pixels: MxNx3 array of pixels
        title: The title of the window

    """
    display_multiple([(pixels, title)])


def write_image_from_rgb_sensor_data(sensor_data, base_path, name):
    """For use in saving `expected` images from RGB camera sensor data

    Args:
        sensor_data: Data from RGB sensor tick
        base_path: Path to test directory containing `expected` directory
        name: Name of file to save, not including `png` file extension
    """
    pixels = sensor_data[:, :, 0:3]
    cv2.imwrite(os.path.join(base_path, "expected", f"{name}.png"), pixels)
