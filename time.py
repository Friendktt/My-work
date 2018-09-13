"""time"""
def main():
    """time"""
    text = input()
    num = int(input())
    mounth = 'JAN FEB MAR APR MAY JUN JUL AUG SEP OCT NOV DEC'
    num1 = mounth.find(text)
    num2 = (num1 + num*4) % 48
    print(mounth[num2:num2 + 3])
main()
