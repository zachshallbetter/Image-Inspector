import argparse
import fitz  # PyMuPDF


def identify_layers(pdf_path):
    # Load the PDF file
    pdf = fitz.open(pdf_path)

    # Extract information about layers (OCGs)
    layers = pdf.get_ocgs()
    layer_info = {layer.name: layer for layer in layers}

    # List existing layers
    existing_layers = list(layer_info.keys())
    return existing_layers


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Inspector Layer Identification")
    parser.add_argument("--input", required=True, help="Path to the input PDF file")
    args = parser.parse_args()

    pdf_path = args.input
    layers = identify_layers(pdf_path)
    print("Identified Layers:")
    print(layers)
