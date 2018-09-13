"""secu"""
def main():
    """secu"""
    url = input()
    num1 = url.find('r=')
    num2 = url.find('&')
    num3 = url.find('d=')
    print(url[num1+2:num2])
    print(url[num3+2:])
main()
