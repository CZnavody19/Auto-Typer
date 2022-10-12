from curses.ascii import isupper
from pytesseract import image_to_string, pytesseract
from PIL import ImageGrab
from cv2 import cvtColor, COLOR_BGR2GRAY
from numpy import array
from time import sleep
from keyboard import add_hotkey, wait, press, release, hook_key
from random import random
from string import ascii_lowercase

def parse_bool(input):
    input = input.lower()
    if(input == "n" or input == "no" or input == "0" or input == "false" or input == "f"):
        return False
    elif(input == "y" or input == "yes" or input == "1" or input == "true" or input == "t"):
        return True
    else:
        return None

repeat = int(input("Repeat (num): "))
reverse = parse_bool(input("Reverse (bool): "))
contain = input("Contain (char): ")

text = ""

def main():
    pytesseract.tesseract_cmd = r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

    add_hotkey("windows + shift + s", start)

    wait("ctrl + enter")


def start():
    global text

    sleep(5)

    for letter in ascii_lowercase + " ,":
        hook_key(letter, typeLetter, suppress=True)

    text = capture()

    print("To type: " + text)

def typeLetter(param):
    global text
    if len(text) != 0:
        if param.event_type == "down":
            if text[0].isupper():
                press("shift")
                press(text[0].lower())
                sleep(random()*0.1)
                release(text[0].lower())
                release("shift")
            else:
                press(text[0].lower())
                sleep(random()*0.1)
                release(text[0].lower())
            text = text[::-1][:-1][::-1]

def capture():
    screenshot = ImageGrab.grabclipboard()
    if(screenshot != None):
        text = image_to_string(cvtColor(array(screenshot), COLOR_BGR2GRAY))
        text = text * repeat
        if reverse:
            text = text[:-1]
            text = text[::-1]

        words = text.split()

        if contain == "":
            return ' '.join(words)

        else:
            out = []
            for word in words:
                if contain in word:
                    out.append(word)
            return ' '.join(out)

if __name__ == "__main__":
    main()