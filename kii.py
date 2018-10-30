"""Fiba"""
import math
def main():
    """fiba"""
    num = int(input())
    var = ((1+math.sqrt(5))**num-(1-math.sqrt(5))**num)/(2**num*math.sqrt(5))
    print(int(var))
main()
