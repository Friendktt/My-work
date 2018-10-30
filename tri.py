"""Tri"""
import json
def main():
    """tribic"""
    num = input()
    buk = json.loads(num)
    loop = int(input())
    forward = 0
    mid = 1
    back = 2
    if loop <= 3:
        print(buk[0:loop])
    else:
        for _ in range(loop-3):
            buk.append(buk[forward] + buk[mid] + buk[back])
            forward += 1
            mid += 1
            back += 1
        print(buk)
main()
