"""Auto"""
def main():
    """count"""
    num = "ZERO,ONE,TWO,THREE,FOUR,FIVE,SIX,SEVEN,EIGHT,NINE"
    num = num.split(",")
    tex = input()
    tex = tex.upper()
    ttt = len(tex)
    che = 0
    for i in range(10):
        mon = 0
        for i in tex:
            if i in num[che]:
                mon += 1
            if mon == ttt:
                print(che)
                break
        che += 1
main()
