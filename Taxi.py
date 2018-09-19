"""Taxi"""
import math
def main():
    """mainfunction"""
    distance = int(input())
    time = int(input())
    var1 = time/60
    var2 = math.ceil(var1)
    if 0 <= distance <= 1:
        print(math.ceil(var2*1.5)+50)
    elif 2 <= distance <= 10:
        total = ((var2*1.5)+((distance-1)*5)+50)
        print(math.ceil(total))
    elif 11 <= distance <= 20:
        total = ((var2*1.5)+((distance-10)*7.5)+50+45)
        print(math.ceil(total))
    elif 21 <= distance <= 40:
        total = ((var2*1.5)+((distance-20)*10)+50+45+75)
        print(math.ceil(total))
    elif 41 <= distance <= 65:
        total = ((var2*1.5)+((distance-40)*12.5)+50+45+75+200)
        print(math.ceil(total))
    else:
        total = ((var2*1.5)+((distance-65)*15)+50+45+75+200+312.5)
        print(math.ceil(total))
main()
