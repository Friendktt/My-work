"""CAA"""
def main():
    """mainfunction"""
    text = input()
    if text == text.lower():
        print(chr((ord(text) + 23) * (99 >= ord(text) >= 97)\
        + (ord(text)-3) * (122 >= ord(text) >= 100) + (ord(text) *\
            (96 >= ord(text) or ord(text) >= 123))))
    elif text == text.upper():
        print(chr((ord(text) + 23) * (67 >= ord(text) >= 65)\
        + (ord(text)-3) * (90 >= ord(text) >= 68) + (ord(text) *\
            (64 >= ord(text) or ord(text) >= 91))))
main()
