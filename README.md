# TextAdder

TextAdder is a simple Python script that allows you to add subtitles to a video or text to an image using OpenCV. You can customize the position, font size, and color of the text.

## Features
- Add subtitles to a video.
- Add text to an image.
- Customize the position, font size, and color of the text.

## Prerequisites
- Python 3.x
- OpenCV

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/textadder.git
    cd textadder
    ```

2. Install the required packages:
    ```bash
    pip install opencv-python
    ```

## Usage
### For Video
1. Run the script:
    ```bash
    python textadder.py
    ```

2. Follow the prompts to enter the input video path, subtitle text, and customize the position, font size, and color if desired.

Example:
```bash
Enter the path of the input video: path/to/your/video.mp4
Enter the subtitle text: Hello World!
Do you want to customize subtitle position? (y/n): y
Enter the subtitle position (x, y): 100, 200
Do you want to customize subtitle font size? (y/n): n
Do you want to customize subtitle font color? (y/n): y
Enter the subtitle font color (R, G, B): 255, 255, 255
