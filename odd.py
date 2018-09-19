"""OddEven"""
def main():
    """mainfunction"""
    numa = int(input())
    numa = abs(numa)
    if numa%2 == 0:
        print("Even")
    else:
        print("Odd")
main()
