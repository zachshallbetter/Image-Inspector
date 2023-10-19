import logging
import os

# Create handlers
info_handler = logging.FileHandler(os.path.join("log", "info.log"))
info_handler.setLevel(logging.INFO)

error_handler = logging.FileHandler(os.path.join("log", "error.log"))
error_handler.setLevel(logging.ERROR)

# create a logging object
logger = logging.getLogger()
logger.setLevel(logging.INFO)  # better to have too much log than not enough

# format the logs
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
info_handler.setFormatter(formatter)
error_handler.setFormatter(formatter)

# add the handlers to the logger
logger.addHandler(info_handler)
logger.addHandler(error_handler)

# logging example
logger.info("This is an informational message.")
logger.error("This is an error message.")
from src.config.config_loader import load_config

# Load the configuration
config_path = "./src/config/config.json"
config = load_config(config_path)

# Access configuration options
image_formats = config.get("image_formats", [])
font_recognition_enabled = config.get("enable_font_recognition", False)
max_image_size = config.get("max_image_size", 10)
