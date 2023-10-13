# Create the Inspector project directory
mkdir Inspector

# Move into the Inspector directory
cd Inspector

# Create the config file
mkdir config
touch config/config.json

# Create the source code directory and subdirectories
mkdir src
touch src/__init__.py
touch src/analysis.py
touch src/color.py
touch src/layers.py
touch src/fonts.py
touch src/utils.py

# Create the tests directory and subdirectories
mkdir tests
touch tests/__init__.py
touch tests/test_analysis.py
touch tests/test_color.py
touch tests/test_layers.py
touch tests/test_fonts.py
touch tests/test_utils.py

# Create the main script
touch inspector.py

# Create the requirements.txt file
touch requirements.txt

# Create the README.md file (you can edit it later with documentation)
touch README.md

# Create the data directory for sample data (optional)
mkdir data

# Navigate back to the root directory (optional)
cd ..
