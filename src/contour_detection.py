import cv2
import numpy as np
from typing import List, Tuple


def load_image(image_path: str) -> np.ndarray:
    # Load the image
    return cv2.imread(image_path)


def convert_to_gray(image: np.ndarray) -> np.ndarray:
    # Convert the image to grayscale
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


def apply_gaussian_blur(
    image: np.ndarray, kernel_size: Tuple[int, int] = (5, 5)
) -> np.ndarray:
    # Apply Gaussian blur to the image
    return cv2.GaussianBlur(image, kernel_size, 0)


def detect_edges(
    image: np.ndarray, lower_threshold: int = 50, upper_threshold: int = 150
) -> np.ndarray:
    # Perform edge detection
    return cv2.Canny(image, lower_threshold, upper_threshold)


def dilate(image: np.ndarray, iterations: int = 2) -> np.ndarray:
    # Perform a dilation to close gaps in between object edges
    return cv2.dilate(image, None, iterations=iterations)


def erode(image: np.ndarray, iterations: int = 1) -> np.ndarray:
    # Perform an erosion to further refine object edges
    return cv2.erode(image, None, iterations=iterations)


def find_contours(image: np.ndarray) -> List[np.ndarray]:
    # Find contours in the eroded image
    contours, _ = cv2.findContours(
        image.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
    )
    return contours


def is_color_match(
    color: Tuple[int, int, int], threshold: Tuple[int, int, int]
) -> bool:
    # Function to approximate color matching
    r, g, b = color
    r_threshold, g_threshold, b_threshold = threshold
    return r > r_threshold and g < g_threshold and b > b_threshold


def extract_paths(pdf, page_number: int = 0) -> List[dict]:
    # Extract 'cutcontour' path positions
    page = pdf[page_number]  # Assuming relevant info is on the first page
    return page.get_drawings()


def filter_paths(
    paths: List[dict], color_threshold: Tuple[int, int, int]
) -> List[dict]:
    filtered_paths = []
    for path in paths:
        if "items" in path:
            for item in path["items"]:
                if "fill" in item and is_color_match(item["fill"], color_threshold):
                    filtered_paths.append(item["rect"])  # rect contains the coordinates
    return filtered_paths
