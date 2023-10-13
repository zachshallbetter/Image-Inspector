# src/basic_image_analysis.py

from PIL import Image
import argparse


def analyze_image(image_path):
    # Implement basic image analysis here
    # Extract dimensions, color profiles, and embedded text
    with Image.open(image_path) as img:
        width, height = img.size
        color_profile = img.mode
        # Perform initial text extraction using OCR libraries
        # Example using Tesseract:
        # text = extract_text_with_tesseract(img)

    return {
        "Dimensions": (width, height),
        "Color Profile": color_profile,
        "Embedded Text": text,  # Replace with actual extracted text
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Inspector Basic Image Analysis")
    parser.add_argument("--input", required=True, help="Path to the input image file")
    args = parser.parse_args()

    image_path = args.input
    analysis_result = analyze_image(image_path)
    print("Basic Image Analysis Result:")
    print(analysis_result)
