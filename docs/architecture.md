# Inspector Project Architecture

This document provides an overview of the architecture of the Inspector project.

## Table of Contents

- [Inspector Project Architecture](#inspector-project-architecture)
  - [Table of Contents](#table-of-contents)
  - [Overview](#overview)
  - [Project Structure](#project-structure)
  - [Components](#components)
    - [Inspector Core](#inspector-core)
    - [Image Analysis](#image-analysis)
    - [Configuration](#configuration)
  - [Dependencies](#dependencies)

## Overview

Inspector is designed as a command-line tool for image comprehension in print-and-cut shops. Its architecture is modular and organized to facilitate extensibility and maintainability.

## Project Structure

Inspector follows a well-structured layout to separate concerns and promote maintainability:

- `src/`: Contains the main source code of the project.
- `config/`: Configuration files and loaders.
- `tests/`: Unit tests.
- `docs/`: Documentation files.

## Components

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

Inspector's behavior can be customized through a JSON configuration file (`config/config.json`). This configuration file defines options such as supported image formats, font recognition settings, and more.

## Dependencies

Inspector relies on several Python libraries and packages, including:
- Pillow for image processing.
- pytesseract for OCR (font recognition).
- PyPDF2 for PDF handling.
- ai2pdf and eps2pdf for AI and EPS to PDF conversion.

For a complete list of dependencies, refer to the `requirements.txt` file.

