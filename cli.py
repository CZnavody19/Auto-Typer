import typer

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
    contain = input("Contain: ")
    begins = input("Begins with: ")

    with open("blocked_keys.txt", "r") as blocked_keys_txt:
        additional_blocked_keys = blocked_keys_txt.read()

    input("Enter to parse clipboard image: ")
    text = typer.capture(repeat, reverse, contain, begins)

    print("Text to type: " + text)

    input("Enter to hook keys: ")
    text = typer.start_typing(text, additional_blocked_keys)

if __name__ == "__main__":
    main()