# Multilingual Machine Translation App

This is a multilingual machine translation app that allows users to translate text between multiple languages. The app utilizes an open-source model from Hugging Face and is deployed on Hugging Face Spaces.


## Demo Video

Watch the demo video to see how to run the app:

[![Watch the video](https://img.youtube.com/vi/6i95sySWsvw/maxresdefault.jpg)](https://www.youtube.com/watch?v=6i95sySWsvw)

## Model and App Links

- **Hugging Face Model Link:** [NLLB-200 Distilled 600M](https://huggingface.co/facebook/nllb-200-distilled-600M)
- **App Link:** [Multilingual Machine Translation App](https://huggingface.co/spaces/mahmudunnabi/Multilingual_Machine_Translation_App)

## Prerequisites

To run the app locally, you need to have `ffmpeg` and `espeak` installed on your system. You can install them using the following commands:

### For ffmpeg

- **On Ubuntu:**
  ```bash
  sudo apt update
  sudo apt install ffmpeg


- **On macOS:**
  ```bash
  brew install ffmpeg

## Downloading FFmpeg for Windows

To download FFmpeg for Windows, please follow these steps:

1. Go to the official [FFmpeg download page](https://ffmpeg.org/download.html).

2. Select the appropriate version for Windows and download the zip file.

3. Extract the zip file to a directory of your choice.

For detailed instructions and further information, please refer to the [official FFmpeg documentation](https://ffmpeg.org/documentation.html).

## Downloading eSpeak

### macOS

1. Install eSpeak using Homebrew:
   ```sh
   brew install espeak


### Ubuntu

To install eSpeak using `apt-get`, run the following commands in your terminal:

        ```sh
        sudo apt-get update
        sudo apt-get install espeak


### Windows

To install eSpeak on Windows, follow these steps:

1. Download the eSpeak installer from the [official eSpeak download page](http://espeak.sourceforge.net/download.html).
2. Run the installer.
3. Follow the on-screen instructions to complete the installation.

## Run Locally

To run the app locally, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/your_username/your_repo_name.git

2. Navigate to the project directory:

    ```bash
    cd your_repo_name

3. Install required dependencies
    ```bash
    pip install -r requirements.txt

4. Run the app:
    ```bash
    python app.py

