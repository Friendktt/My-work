"""St"""
def main():
    """St"""
    prod = input()
    price = int(input())
    weigh = int(input())
    code = input()
    day = int(input())
    mont = int(input())
    year = int(input())
    year1 = int(input())
    year2 = year + year1
    print("Name:\t%s" %prod)
    print("Price:\t%d" %price)
    print("Weight:\t%d" %weigh)
    print("ID:\t%s" %code)
    print("EXP:\t%02d/%02d/%04d" %(day, mont, year2))
main()
