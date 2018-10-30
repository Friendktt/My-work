"""Superdance"""
def main():
    """dace"""
    num = int(input())
    for i in range(num):
        drop = int(input())
        sta = input()
        stb = input()
        mix1 = 0
        poss = 0
        cout = 0
        for i in range(drop):
            che = 0
            if sta[i] == stb[i]:
                che = 1
                cout += 1
            if che == 1 and cout >= 1:
                mix1 += 1
                poss += mix1
            else:
                mix1 = 0
                cout = 0
        print(poss)
main()
