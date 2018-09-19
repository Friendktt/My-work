"""Direct"""
def main():
    """mainfunction"""
    numx = int(input())
    numy = int(input())
    if numx == 0 and numy > 0:
        print("North")
    elif numx > 0 and numy == 0:
        print("East")
    elif numx == 0 and numy < 0:
        print("South")
    elif numx < 0 and numy == 0:
        print("West")
    elif numx > 0 and numy > 0:
        print("Northeast")
    elif numx > 0 and numy < 0:
        print("Southeast")
    elif numx < 0 and numy < 0:
        print("Southwest")
    elif numx < 0 and numy > 0:
        print("Northwest")
    elif numx == 0 and numy == 0:
        print("Origin")
main()
