"""CHA"""
def main():
    """CHA"""
    num1 = int(input())
    mounth = "January   February  March     April     May       June      July      \
August    September October   November  December  "
    print(mounth[int((num1-1)/(0.1)):int(num1/(0.1))])
main()
