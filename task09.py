a = float(input("1-tomon uzunligini kiriting: "))
b = float(input("2-tomon uzunligini kiriting: "))
c = float(input("3-tomon uzunligini kiriting: "))

if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print(" by teng tomonli uchburchak")
    elif a == b or a == c or b == c:
        print("bu teng yoni uchburchak")
    else:
        print(' bu turli tomonli uchburchak')
else:
    print("Bu tomonlar bilan uchburchak hosil bolmaydi")
