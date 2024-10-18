# Stable Diffusion Avatar Generator

This project is a Streamlit-based web application that generates custom avatars using the Fooocus API, which is built on Stable Diffusion. Users can input prompts, set parameters, and generate unique avatar images.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Configuration](#configuration)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.7 or higher
- Fooocus installed on your system
- Streamlit

## Installation

1. Clone this repository to your local machine.
2. Install the required Python packages:
   ```
   pip install streamlit pillow
   ```
3. Set up Fooocus:

   - Follow the installation instructions for Fooocus from their official repository.
   - Note the path where Fooocus is installed.

4. Update the `FOOOCUS_PATH` variable in the script:
   ```python
   FOOOCUS_PATH = r"C:\path\to\your\Fooocus-main"
   ```

## Usage

To run the Stable Diffusion Avatar Generator:

1. Navigate to the project directory in your terminal.
2. Run the Streamlit app:
   ```
   streamlit run app.py
   ```
3. Open your web browser and go to the URL provided by Streamlit (usually `http://localhost:8501`).

## Features

- Generate custom avatars based on text prompts
- Customize negative prompts for better results
- Choose from different style presets
- Adjust the number of generation steps
- Download generated avatars

## Configuration

You can customize the following parameters in the application:

- Prompt: Describe the avatar you want to generate
- Negative prompt: Specify what you don't want in the image
- Style: Choose from "Fooocus V2", "Fooocus Enhance", or "Fooocus Sharp"
- Number of steps: Adjust the generation steps (20-100)

Advanced users can modify the `params` dictionary in the `generate_avatar` function to fine-tune the generation process.

## Troubleshooting

If you encounter any issues:

1. Ensure Fooocus is properly installed and the path is correctly set.
2. Check that all required Python packages are installed.
3. Verify that you have sufficient GPU memory (if using GPU acceleration).

For persistent problems, check the Fooocus documentation or open an issue in this project's repository.

## Contributing

Contributions to this project are welcome. Please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
