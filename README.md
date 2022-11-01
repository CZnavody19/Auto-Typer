# Auto-Typer
### Hooks your keys to only type the thing you selected.

## Installation

You need to download [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) for your OS. [Here](https://tesseract-ocr.github.io/tessdoc/Installation.html) is a guide.

**Warning:** You need to install to the default location which is `C:\\Program Files\\Tesseract-OCR`
 
You also need [Python](https://www.python.org/) with pip and tkinter.

The pip packages needed are [here](requirements.txt). Install them with `pip install -r requirements.txt`

## How to use

### Command Line
- Run the [comand line script](cli.py)
- Enter the number of times to repeat the text
- Enter wherever to reverse the text or not
- Enter what characters the text should contain (`Enter` for everything)
- Enter what characters the text should begin with (`Enter` for everything)

- Press `Windows Shift S` and select the area of the text
- Press `Enter` to detect the text
- Wait until the program displays the text
- Press `Enter` to start typing
- Then start typing, the program will "rewrite" the keys to the correct ones (By default only letters are enabled. To enable additional keys enter them to the [file](blocked_keys.txt).)
- At the end press `Ctrl Enter` to stop the program

### GUI
- Run the [GUI script](gui.py)
- Configure the parameters
- Press `Windows Shift S` and select the area of the text
- Click `Capture` and review the text
- Click `Start` and start typing, the program will "rewrite" the keys to the correct ones (By default only letters are enabled. To enable additional keys enter them to the [file](blocked_keys.txt).)