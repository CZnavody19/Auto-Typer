from pytesseract import image_to_string, pytesseract
from PIL import ImageGrab
from cv2 import cvtColor, COLOR_BGR2GRAY
from numpy import array
from time import sleep
from keyboard import add_hotkey, wait, hook_key, write
from string import ascii_lowercase

def parse_bool(input):
    input = input.lower()
    if(input == "n" or input == "no" or input == "0" or input == "false" or input == "f"):
        return False
    elif(input == "y" or input == "yes" or input == "1" or input == "true" or input == "t"):
        return True
    else:
        return None

repeat = int(input("Repeat: "))
reverse = parse_bool(input("Reverse: "))
contain = input("Contain: ")
begins = input("Begins with: ")

with open("blocked_keys.txt", "r") as blocked_keys_txt:
    additional_blocked_keys = blocked_keys_txt.read()

text = ""

def main():
    pytesseract.tesseract_cmd = r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

    add_hotkey("windows + shift + s", start)

    wait("ctrl + enter")


def start():
    global text

    sleep(5)

    for letter in ascii_lowercase + additional_blocked_keys:
        hook_key(letter, typeLetter, suppress=True)

    text = capture()

    print("To type: " + text)

def typeLetter(param):
    global text
    if len(text) != 0:
        if param.event_type == "down":
            write(text[0])
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

        if contain == "" and begins == "":
            return ' '.join(words)

        elif contain != "":
            out = []
            for word in words:
                if contain in word:
                    out.append(word)
            return ' '.join(out)

        elif begins != "":
            out = []
            for word in words:
                if word[0] == begins:
                    out.append(word)
            return ' '.join(out)

if __name__ == "__main__":
    main()