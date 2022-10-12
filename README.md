# Auto-Typer
### Hooks your keys to only type the thing you selected.

## Installation

You need to download [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) for your OS. [Here](https://tesseract-ocr.github.io/tessdoc/Installation.html) is a guide.

**Warning:** You need to install to the default location which is `C:\\Program Files\\Tesseract-OCR`
 
You also need [Python](https://www.python.org/) with pip.

The pip packages needed are [here](requirements.txt). Install them with `pip install -r requirements.txt`

## How to use

- Run the [script](main.py)
- Enter the number of times to repeat the text
- Enter wherever to reverse the text or not
- Enter what characters the text should contain (Enter for everything)

- Press `Windows Shift S` and select the area of the text (You have about 5 seconds from pressing the shortcut to the program starting)
- Wait until the program displays the text
- Then start typing, the program will "rewrite" the keys to the correct ones (By default only letters are enabled. To enable additional keys enter them to the [file](blocked_keys.txt).)
- At the end press `Ctrl Enter` to stop the program