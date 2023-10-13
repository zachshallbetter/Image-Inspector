from src.config.config_loader import load_config

# Load the configuration
config_path = "config/config.json"
config = load_config(config_path)

# Access configuration options
image_formats = config.get("image_formats", [])
font_recognition_enabled = config.get("enable_font_recognition", False)
max_image_size = config.get("max_image_size", 10)

# Use the configuration in your Inspector application
