"""SELFDESNUM"""
def main():
    """numlinkinpark"""
    tex = input()
    tex = tex[1:-1]
    emp = []
    i = 0
    moo = ""
    for i in range(len(tex)):
        if i >= 10:
            i = 999999
        poss = tex.count(str(i))
        emp.append(poss)
    for i in emp:
        moo += str(i)
    if moo == tex:
        print("YES")
    else:
        print("NO")
main()
