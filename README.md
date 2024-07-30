# League of Legends Auto-Accept Match Bot

This Python program automatically accepts a match in League of Legends by detecting the "Accept" button on the screen using image processing techniques. The program uses NumPy and OpenCV to process screenshots and locate the button.

## Features

- Uses NumPy and OpenCV for image processing.
- Takes a screenshot of the screen and converts it to grayscale for easier processing.
- Uses template matching to locate the "Accept" button on the screen.
- Clicks the "Accept" button once it is detected.
- Ends the program after accepting the match.

## Prerequisites

Before running the program, ensure you have the following installed:

- Python 3.x
- NumPy
- OpenCV
- PyAutoGUI

## How it Works
- The program continuously takes screenshots of the current screen.
- Each screenshot is converted to grayscale for easier processing.
- The reference image of the “Accept” button is also converted to grayscale.
- The program uses template matching to find the “Accept” button in the screenshot.
- If a strong match is found (above the threshold), the program clicks the center of the detected button.
- The program prints “Match Accepted!” and ends.

You can install the required packages using pip:

```bash
pip install numpy opencv-python pyautogui
