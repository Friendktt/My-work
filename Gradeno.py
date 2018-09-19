"""GradeNoIF"""
def main():
    """mainfunction"""
    score = int(input())
    print(("0"*(0 <= score <= 49)) + ("1"*(50 <= score <= 54))\
    +("1.5"*(55 <= score <= 59)) + ("2"*(60 <= score <= 64))\
    +("2.5"*(65 <= score <= 69)) + ("3"*(70 <= score <= 74))\
    +("3.5"*(75 <= score <= 79)) + ("4"*(80 <= score <= 100))\
    +("Invalid"*(100 < score or score < 0)))
main()
