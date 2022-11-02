from pytesseract import image_to_string, pytesseract
from PIL import ImageGrab
from cv2 import cvtColor, COLOR_BGR2GRAY
from numpy import array
from keyboard import hook_key, write, wait, unhook_all
from string import ascii_lowercase

text = ""
pytesseract.tesseract_cmd = r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

def start_typing(text_to_type, blocked_keys):
    global text
    text = text_to_type
    for letter in ascii_lowercase + blocked_keys:
        hook_key(letter, typeLetter, suppress=True)
    wait("ctrl + enter")
    unhook_all()

def typeLetter(param):
    global text
    if len(text) != 0:
        if param.event_type == "down":
            write(text[0])
            text = text[::-1][:-1][::-1]

def capture(repeat, reverse, contain, begins, nospace):
    screenshot = ImageGrab.grabclipboard()
    if(screenshot != None):
        text = image_to_string(cvtColor(array(screenshot), COLOR_BGR2GRAY))
        text = text * repeat
        if reverse:
            text = text[:-1]
            text = text[::-1]

        if nospace:
            text = text.replace(" ", "")

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