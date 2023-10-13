import json


def load_config(config_path):
    try:
        with open(config_path, "r") as config_file:
            config = json.load(config_file)
        return config
    except FileNotFoundError:
        print("Configuration file not found.")
        return {}


# Example usage
if __name__ == "__main__":
    config_path = "src/config/config.json"
    config = load_config(config_path)

    # Access configuration options
    image_formats = config.get("image_formats", [])
    font_recognition_enabled = config.get("enable_font_recognition", False)
    max_image_size = config.get("max_image_size", 10)

    print("Image Formats:", image_formats)
    print("Font Recognition Enabled:", font_recognition_enabled)
    print("Max Image Size (MB):", max_image_size)
