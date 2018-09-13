"""inver"""
def main():
    """inver"""
    num = str(input())
    num1 = num.replace('0', '2')
    num2 = num1.replace('1', '0')
    num3 = num2.replace('2', '1')
    print(num3)
main()
