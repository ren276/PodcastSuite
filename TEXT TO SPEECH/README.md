# Advanced Multilingual Text-to-Speech Converter

This Streamlit-based web application converts text to speech in multiple languages using the edge-tts library. It offers a user-friendly interface for generating high-quality speech output with various voice options and adjustable speech rates.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Supported Languages](#supported-languages)
- [Configuration](#configuration)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)

## Features

- Support for multiple languages and accents
- Male and female voice options for most languages
- Adjustable speech rate (Very Slow to Very Fast)
- Real-time audio playback in the browser
- Option to download the generated audio file
- User-friendly interface with Streamlit
- Informative sidebar with supported languages and features

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.7 or higher
- pip (Python package manager)

## Installation

1. Clone this repository to your local machine:

   ```
   git clone https://github.com/yourusername/multilingual-tts-converter.git
   cd multilingual-tts-converter
   ```

2. Install the required Python packages:
   ```
   pip install streamlit edge-tts
   ```

## Usage

To run the Advanced Multilingual Text-to-Speech Converter:

1. Navigate to the project directory in your terminal.
2. Run the Streamlit app:
   ```
   streamlit run app.py
   ```
3. Open your web browser and go to the URL provided by Streamlit (usually `http://localhost:8501`).
4. Enter the text you want to convert to speech in the text area.
5. Select a voice and speech rate from the dropdown menus.
6. Click the "Convert to Speech" button to generate the audio.
7. Use the audio player to listen to the generated speech or click the download link to save the audio file.

## Supported Languages

The application supports a wide range of languages, including but not limited to:

- English (US and UK)
- Spanish (Spain and Mexico)
- French
- German
- Italian
- Japanese
- Chinese (Mandarin)
- Hindi
- Arabic
- Russian
- Portuguese (Brazil)
- Korean

For a complete list of supported languages and voices, refer to the sidebar in the application.

## Configuration

You can customize the following parameters in the application:

- Text input: Enter the text you want to convert to speech
- Voice selection: Choose from various language and gender options
- Speech rate: Select from Very Slow, Slow, Normal, Fast, or Very Fast

Advanced users can modify the `VOICES` dictionary in the script to add or remove voice options.

## Troubleshooting

If you encounter any issues:

1. Ensure all required Python packages are installed correctly.
2. Check your internet connection, as edge-tts requires an active connection to function.
3. Verify that you're using a compatible browser for audio playback.

For persistent problems, please open an issue in this project's repository.

## Contributing

Contributions to this project are welcome. Please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
