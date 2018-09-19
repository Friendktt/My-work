"""Bigcock"""
def main():
    """mainfunction"""
    numb = input().split(" ")
    hour = int(numb[0])
    minite = int(numb[1])
    hour_k = (hour+minite/60)*30
    minite_k = minite*6
    if hour_k == minite_k:
        print("True")
    elif 0 <= hour_k - minite_k < 6:
        print("True")
    else:
        print("False")
main()
