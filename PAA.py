"""PA"""
def main():
    """mainfunction"""
    text = input()
    textre = text[::-1]
    if text == textre:
        print("%s is Palindrome."%text)
    else:
        print("This is not Palindrome")
main()
