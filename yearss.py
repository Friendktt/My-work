"""Year"""
def main():
    """mainfunction"""
    years = int(input())
    if years%100 == 0:
        if years%400 == 0:
            print('%d is a leap year.'%years)
        else:
            print('%d is not a leap year.'%years)
    else:
        if years%4 == 0:
            print('%d is a leap year.'%years)
        else:
            print('%d is not a leap year.'%years)
main()