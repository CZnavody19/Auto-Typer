import typer
import json

def parse_bool(input):
    input = input.lower()
    if(input == "n" or input == "no" or input == "0" or input == "false" or input == "f"):
        return False
    elif(input == "y" or input == "yes" or input == "1" or input == "true" or input == "t"):
        return True
    else:
        return None

def main():
    repeat = int(input("Repeat: "))
    reverse = parse_bool(input("Reverse: "))
    nospace = parse_bool(input("No spaces: "))
    contain = input("Contain: ")
    begins = input("Begins with: ")

    with open("options.json", "r") as options:
        parsed_options = json.load(options)

    input("Enter to parse clipboard image: ")
    text = typer.capture(repeat, reverse, contain, begins, nospace)

    print("Text to type: " + text)

    input("Enter to hook keys: ")
    text = typer.start_typing(text, parsed_options["blocked_keys"])

if __name__ == "__main__":
    main()