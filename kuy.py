"""look e mam"""
def main():
    """kuy"""
    text1 = input()
    text2 = input()
    num1 = int(input())
    num2 = int(input())
    text1re = text1[::-1]
    text2re = text2[::-1]
    char1 = text1re[(num1-1)]
    char2 = text2re[(num2-1)]
    print(ord(char1)+ord(char2))
main()
