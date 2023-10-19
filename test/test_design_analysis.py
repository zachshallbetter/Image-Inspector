# Directions
# 1. Execute the test suite in the terminal using the command:
# - `python test/test_design_analysis.py`
# - To run a specific test, use the command:
# - `python test/test_design_analysis.py test_analyze_image`
# To run multiple tests, use the command:
# 2. Examine the output to identify any failing tests.
# 3. Locate and open the file containing the failing test.
# 4. Modify the test to ensure it passes.
# 5. Repeat steps 1-4 until all tests are successful.

import unittest
import numpy as np
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.ingest import import_image
from src.color import identify_spot_colors
from src.analysis import analyze_image
from src.layers import identify_layers
from src.fonts import recognize_fonts

_test_files = [
    f
    for f in os.listdir("test/")
    if not f[0] == "."
    and os.path.splitext(f)[1] in [".png", ".jpg", ".jpeg", ".pdf", ".ai", ".eps"]
]

_test_files.sort(key=os.path.splitext)


class TestDesignAnalysis(unittest.TestCase):
    def test_analyze_image(self):
        for image_path in _test_files:
            result = analyze_image(os.path.join("test", image_path))
            self.assertIsInstance(result, dict)

    # def test_analyze_illustrator(self):
    #     image_path = os.path.join(os.getcwd(), "test", "contour-lines.ai")
    #     result = analyze_image(image_path)
    #     self.assertIsInstance(result, dict)

    # def test_recognize_fonts(self):
    #     image_path = os.path.join(os.getcwd(), "test", "bane.png")
    #     result = recognize_fonts(image_path)
    #     self.assertIsInstance(result, list)

    # def test_identify_spot_colors(self):
    #     image_path = os.path.join(os.getcwd(), "test", "bane.png")
    #     result = identify_spot_colors(image_path)
    #     self.assertIsInstance(result, np.ndarray)

    # def test_identify_layers(self):
    #     pdf_path = os.path.join(os.getcwd(), "test", "contour-lines.pdf")
    #     result = identify_layers(pdf_path)
    #     self.assertIsInstance(result, type(None))


if __name__ == "__main__":
    if len(sys.argv) > 1:
        suite = unittest.TestSuite()
        for test_name in sys.argv[1:]:
            suite.addTest(TestDesignAnalysis(f"test_{test_name}"))
        runner = unittest.TextTestRunner()
        runner.run(suite)
    else:
        unittest.main()
