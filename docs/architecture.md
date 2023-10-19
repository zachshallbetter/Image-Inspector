# Inspector Project Architecture

This document provides an overview of the architecture of the Inspector project.

## Table of Contents

- [Inspector Project Architecture](#inspector-project-architecture)
  - [Table of Contents](#table-of-contents)
  - [Overview](#overview)
  - [Project Structure](#project-structure)
    - [To Add](#to-add)
  - [Components](#components)
    - [Inspector Core](#inspector-core)
    - [Image Analysis](#image-analysis)
    - [Configuration](#configuration)
  - [Dependencies](#dependencies)
  - [Extensibility](#extensibility)

## Overview

Inspector is designed as a command-line tool for image comprehension in print-and-cut shops. Its architecture is modular and organized to facilitate extensibility and maintainability.

## Project Structure

Inspector follows a well-structured layout to separate concerns and promote maintainability:

- `/tests/`: Unit tests.
- `/docs/`: Documentation files.
- `/data/`: Sample data for testing.
- `/src/`: Contains the main source code of the project.
- `/src/config/: Configuration files and loaders.
- `/logs/`: Log files for debugging and error tracking.
- `/assets/`: Static files like images, fonts, etc.

### To Add
- `/src/utils/`: Utility scripts and helper functions.
- `/src/modules/`: Individual modules for each functionality.
- `/src/cli/`: Command-line interface scripts.
- `/src/lib/`: External libraries and dependencies.

## Components
The Inspector project is composed of several key components:

- **Inspector Core**: This is the main component responsible for command-line interaction, configuration loading, and orchestrating various modules for image analysis.

- **Image Analysis**: This component includes modules for image import, basic image analysis, spot color identification, layer identification, and font recognition using OCR.

- **File Analysis**: This component is responsible for handling and analyzing different file formats, including PDF, AI, and EPS.

- **Adobe Analysis**: This component handles the conversion of AI and EPS files to PDF for further analysis.

- **Configuration**: This component allows customization of Inspector's behavior through multiple JSON configuration files found in the `src/config/` directory.

- **Command Line Interface (CLI)**: This component is responsible for the user interface, allowing users to interact with the tool via command line.

- **File I/O**: This component handles reading and writing files, enabling the tool to ingest data and output results.

- **API**: This component provides a set of functions and procedures allowing the creation of applications that access the features or data of the Inspector tool.

- **Dependencies**: This component includes several Python libraries and packages that Inspector relies on, such as Pillow for image processing, pytesseract for OCR, PyPDF2 for PDF handling, and ai2pdf and eps2pdf for AI and EPS to PDF conversion.

- **Extensibility**: This component is designed for ease of extension. New modules can be added to the `src/` directory, and their configurations can be set in `src/config/`. This modular approach ensures that adding new features will not disrupt existing functionalities.


### Inspector Core

The core component of Inspector is responsible for command-line interaction, configuration loading, and orchestrating various modules for image analysis.

### Image Analysis

Image analysis modules include functionalities for:
- Image import from various formats.
- Basic image analysis (dimensions, color profiles, embedded text).
- Spot color identification.
- Layer identification.
- Font recognition using OCR.

### Configuration

Inspector's behavior can be customized through multiple JSON configuration files found in the `src/config/ directory, including `config.json` and `analysis_config.json`. This configuration file defines options such as supported image formats, font recognition settings, and more.

## Dependencies

Inspector relies on several Python libraries and packages, including:
- Pillow for image processing.
- pytesseract for OCR (font recognition).
- PyPDF2 for PDF handling.
- ai2pdf and eps2pdf for AI and EPS to PDF conversion.

For a complete list of dependencies, refer to the `requirements.txt` file.



## Extensibility
The Inspector tool is architected for ease of extension. New modules can be added to the `src/` directory, and their configurations can be set in `src/config/`. This modular approach ensures that adding new features will not disrupt existing functionalities.

For a list of recommended changes aimed at improving the project, refer to [Recommendations](docs/recommendations.md).

For a comprehensive plan on how to handle parameters in JSON configuration files, refer to [JSON Parameters] (docs/parameters.md).