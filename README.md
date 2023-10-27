# Inspector

Inspector is a command-line tool designed for print-and-cut shops to analyze and comprehend design files in various formats, ensuring they meet specific criteria before proceeding with printing and cutting processes. Inspector focuses on image analysis, offering capabilities for identifying spot colors, layers, fonts, and other essential elements within design files. This tool streamlines the quality control process and aids in error detection, enhancing the efficiency and accuracy of print-and-cut operations.

## Table of Contents

- [Inspector](#inspector)
  - [Table of Contents](#table-of-contents)
  - [Features](#features)
  - [Getting Started](#getting-started)
  - [Running Tests](#running-tests)
  - [Logging](#logging)
  - [Data Directory](#data-directory)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
  - [Usage](#usage)
    - [Installation](#installation-1)
    - [Basic Usage](#basic-usage)
      - [`analyze`](#analyze)
      - [`configure`](#configure)
      - [`list-formats`](#list-formats)
    - [Additional Commands](#additional-commands)
    - [Scripting and Automation](#scripting-and-automation)
    - [Configuration](#configuration)
  - [Project Structure](#project-structure)
  - [Contributing](#contributing)
  - [License](#license)
  - [Additional Documentation](#additional-documentation)
  - [Extending the Tool](#extending-the-tool)

## Features

Inspector offers a range of features to facilitate image comprehension in the context of print-and-cut shops:

- **Image Import:** Support for importing various image file formats, including PDF, AI, EPS, PNG, JPG, TIFF, etc.

- **Basic Image Analysis:** Perform fundamental image analysis to extract dimensions, color profiles, and embedded text from design files.

- **Spot Color Identification:** Detect spot colors within imported images, with the ability to extract color codes and names.

- **Layer Identification:** Identify layers within vector files (AI, EPS) through command-line options.

- **Font Recognition:** Recognize fonts used in both vector and raster images using Optical Character Recognition (OCR).

- **Customizable Configuration:** Easily configure Inspector through a JSON configuration file to adapt it to your specific needs.

## Getting Started

## Running Tests
*Information on how to set up and run tests is missing. Provide guidelines on how to run tests for this application.*

## Logging
*Details about logging mechanisms, where logs are stored, and how to interpret them are missing.*

## Data Directory
*Explain what the `data/` directory is used for and what kind of data is stored there.*

### Prerequisites

To use Inspector, you'll need:

- Python 3.6 or higher installed on your system.

### Installation

1. Clone the Inspector repository to your local machine:

   ```bash
   git clone https://github.com/your-username/Inspector.git
   ```

2. Navigate to the Inspector directory:

   ```bash
   cd Inspector
   ```

3. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   ```

4. Activate the virtual environment:

   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

   - On macOS and Linux:

     ```bash
     source venv/bin/activate
     ```

5. Install the project dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

Inspector provides a Command-Line Interface (CLI) that allows users to interact with the tool using simple commands and options. This section explains how to use the CLI, its available commands, and their associated options.

### Installation

Before using the CLI, make sure you've followed the [Installation](#installation) instructions in the previous section.

### Basic Usage

To invoke Inspector's CLI, open a terminal and use the following command:

```bash
python inspector.py <command> [options]
```

Replace `<command>` with the desired command and `[options]` with any applicable options or arguments. Below are some common CLI commands:

#### `analyze`

The `analyze` command is used to analyze a design file and perform image comprehension. You must specify the path to the design file using the `--input` option. For example:

```bash
python inspector.py analyze --input path/to/design_file.pdf
```

This command initiates the analysis process and provides feedback on the analysis results.

#### `configure`

The `configure` command allows you to customize Inspector's behavior through the CLI. You can set options such as supported image formats, font recognition settings, and more. For example:

```bash
python inspector.py configure --image-formats pdf ai eps png jpg tiff
```

Use the appropriate options and arguments to configure Inspector according to your specific requirements.

#### `list-formats`

The `list-formats` command provides a list of supported image formats that Inspector can process. This can be helpful when configuring supported formats. Use the following command:

```bash
python inspector.py list-formats
```

### Additional Commands

Inspector's CLI offers additional commands and options for more advanced usage and customization. For a complete list of available commands and their descriptions, you can run the following command:

```bash
python inspector.py --help
```

This command displays a list of all available commands and provides brief descriptions of their purposes.

### Scripting and Automation

Inspector's CLI is suitable for scripting and automation tasks. You can integrate Inspector into your existing workflows or use it within automation scripts to streamline your print-and-cut processes.

### Configuration

Inspector's behavior can be configured through the `config/config.json` file. Modify this file to customize settings such as supported image formats, font recognition, and more. Refer to the [Configuration](#configuration) section in this README for details on available configuration options.

## Project Structure

Inspector follows a structured project layout:

- `inspector.py`: The main script for Inspector, providing the command-line interface (CLI).

- `requirements.txt`: A list of project dependencies.

- `README.md`: Documentation for the project, including installation and usage instructions.

- `src/config/: Directory for storing configuration files.
  - `config.json`: JSON file for configuring Inspector's behavior.

- `src/`: Source code directory.
  - `__init__.py`: Initialization script for the `src` module.
  - `image_import.py`: Functions for importing various image formats.
  - `basic_image_analysis.py`: Functions for basic image analysis.
  - `spot_color_identification.py`: Functions for spot color identification.
  - `layer_identification.py`: Functions for layer identification.
  - `font_recognition.py`: Functions for font recognition using OCR.
  - `utils.py`: Utility functions used across modules.

- `tests/`: Directory for unit tests.
  - `__init__.py`: Initialization script for the `tests` module.
  - `test_image_import.py`: Unit tests for image import functions.
  - `test_analysis.py`: Unit tests for image analysis functions.
  - `test_color_identification.py`: Unit tests for spot color identification functions.
  - `test_layer_identification.py`: Unit tests for layer identification functions.
  - `test_font_recognition.py`: Unit tests for font recognition functions.
  - `test_utils.py`: Unit tests for utility functions.
 
## Additional Documentation
For more details on the architecture and functionalities of the Inspector tool, please refer to the following documents in the `docs/` directory:
- [Overview](docs/overview.md)
- [Architecture](docs/architecture.md)

## Extending the Tool
The Inspector tool is designed for extensibility. New modules for additional analyses can be added in the `src/` directory. Configuration for new modules should be placed in `src/config/`.
- [Recommendations](docs/recommendations.md): Suggested improvements for the project.

- [JSON Parameters Strategy](docs/parameters.md): Strategy for managing JSON configuration parameters.


## Contributing

Contributions to Inspector are welcome! If you find any issues or have ideas for enhancements, please open an issue or submit a pull request on the [Inspector GitHub repository](https://github.com/your-username/Inspector).

## License

This project is licensed under the [MIT License](LICENSE).
