"""Grade"""
def main():
    """mainfunction"""
    score1 = int(input())
    if 80 <= score1 <= 100:
        print("4")
    elif 75 <= score1 <= 79:
        print("3.5")
    elif 70 <= score1 <= 74:
        print("3")
    elif  65 <= score1 <= 69:
        print("2.5")
    elif 60 <= score1 <= 64:
        print("2")
    elif 55 <= score1 <= 59:
        print("1.5")
    elif 50 <= score1 <= 54:
        print("1")
    elif 0 <= score1 <= 49:
        print("0")
    else:
        print("Invalid")
main()