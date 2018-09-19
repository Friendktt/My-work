"""Over"""
import math
def main():
    """mainfunction"""
    numx1 = float(input())
    numy1 = float(input())
    rad = float(input())
    numx2 = float(input())
    numy2 = float(input())
    rad2 = float(input())
    var = math.sqrt(((numx2-numx1)**2) + ((numy2-numy1)**2))
    var2 = rad+rad2
    if var2 >= var:
        print("Yes")
    else:
        print("No")
main()
