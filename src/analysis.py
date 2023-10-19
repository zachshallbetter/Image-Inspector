import cv2
import os
import sys
import json
from typing import Dict

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from .color import identify_spot_colors
from .fonts import recognize_fonts
from .layers import identify_layers


def analyze_image(image_path: str) -> Dict:
    print("Analyzing image: ", image_path)

    # Load configurations
    with open("./src/config/analysis_config.json", "r") as f:
        config = json.load(f)

    image = cv2.imread(image_path)

    # Extract text from the image. For now, we set it as an empty string.
    text = (
        ""
        if not config["enable_embedded_text"]
        else "Replace with actual extracted text"
    )
    spot_colors = (
        None if not config["enable_spot_colors"] else identify_spot_colors(image_path)
    )
    fonts = None if not config["enable_fonts"] else recognize_fonts(image_path)
    layers = None if not config["enable_layers"] else identify_layers(image_path)

    result = {
        "Dimensions": image.shape,
        "Size": image.size,
        "Type": image.dtype,
        "Spot Colors": spot_colors,
        "Embedded Text": text,
        "Layers": layers,
        "Fonts": fonts,
    }

    return result
