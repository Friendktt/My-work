"""PASSWORD"""
def main():
    """passtursud"""
    scr = 0
    num2 = 0
    num3 = 0
    num4 = 0
    num5 = 0
    num9 = 0
    maa = 0
    stop = 0
    modi = 0
    for i in range(2):
        num = input()
        num1 = int(len(num))
        cont = num.count(num[0])
        if num1 < 6 and modi == 0:
            print("try again")
            stop += 1
            modi = 2
        if num1 > 5:
            if num.isnumeric() == True:
                scr += 50
            else:
                for i in num:
                    if i.isdigit() == False:
                        num2 = 2
                    if i.isdigit() == True:
                        num3 = 1
                    if i.islower() == True:
                        num4 = 2
                    if i.isupper() == True:
                        num5 = 2
            if num.islower() == True and num2 == 2 \
            and num3 == 0:
                scr += 130
            if num.isupper() == True and num2 == 2 \
            and num3 == 0:
                scr += 115
            if num2 == 2 and num3 == 1:
                scr += 75
            if num4 == 2 and num5 == 2 and num3 == 0:
                scr += 205
            if cont > 4:
                cont = (cont-4)*-15
                scr += cont
            if num1 > 10:
                num9 = (num1-10)*10
                scr += num9
            scr1 = ord(num[-1])+scr
            if scr1 < 150:
                maa = "poor"
            elif scr1 >= 150 and scr1 < 300:
                maa = "acceptable"
            elif scr1 >= 300:
                maa = "secure"
            print("Password : "+ num1*"*")
            print("Security score :", scr1)
            print("Security level :", maa)
            break
        if stop == 2 and modi == 2:
            print("process terminated")
            break
        stop += 1
main()
