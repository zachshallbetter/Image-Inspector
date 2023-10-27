import unittest
import os.path
from src.contour_detection import detect_contours


class TestContours(unittest.TestCase):
    def test_detect_contours(self):
        # Replace with your actual image file path
        image_path = "path_to_your_image_file"

        # Verify the image path exists
        self.assertTrue(os.path.exists(image_path))

        output = detect_contours(image_path)

        # Assert that the output is a list (as expected)
        self.assertTrue(isinstance(output, list))


if __name__ == "__main__":
    unittest.main()
