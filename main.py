kal = "       калькулятор"
print(kal.upper())
chislo = int(input("Введите число - "))
znak = input("Выберите '+','-','*','/' ")
if znak == '+':
    chislo1 = int(input("Введите число - "))
    znak = input("Выберите '+','-','*','/' ")
    if znak == '+':
        chislo2 = int(input("Введите число - "))
        sum1 = chislo + chislo1 + chislo2
        print("  =  " + str(sum1))
    if znak == '-':
        chislo3 = int(input("Введите число - "))
        sum2 = chislo + chislo1 - chislo3
        print("  =  " + str(sum2))
    if znak == '*':
        chislo4 = int(input("Введите число - "))
        sum3 = chislo + (chislo1 * chislo4)
        print("  =  " + str(sum3))
    if znak == '/':
        chislo5 = int(input("Введите число - "))
        sum4 = chislo + (chislo1 / chislo5)
        print("  =  " + str(sum4))

if znak == '-':
    minus1 = int(input("Введите число - "))
    znak = input("Выберите '+','-','*','/' ")
    if znak == '+':
        minus2 = int(input("Введите число - "))
        min0 = chislo - minus1 + minus2
        print("  =  " + str(min0))

    if znak == '-':
        minus3 = int(input("Введите число - "))
        min1 = chislo - minus1 - minus3
        print("  =  " + str(min1))

    if znak == '*':
        minus4 = int(input("Введите число - "))
        min2 = chislo - (minus1 * minus4)
        print("  =  " + str(min2))

    if znak == '/':
        minus5 = int(input("Введите число - "))
        min3 = chislo - (minus1 / minus5)
        print("  =  " + str(min3))

if znak == '*':
    umna = int(input("Введите число - "))
    znak = input("Выберите '+','-','*','/' ")
    if znak == '+':
        umna1 = int(input("Введите число - "))
        um1 = chislo * umna + umna1
        print("  =  " + str(um1))

    if znak == '-':
        umna2 = int(input("Введите число - "))
        um2 = chislo * umna - umna2
        print("  =  " + str(um2))

    if znak == '*':
        umna3 = int(input("Введите число - "))
        um3 = chislo * umna * umna3
        print("  =  " + str(um3))

    if znak == '/':
        umna4 = int(input("Введите число - "))
        um4 = chislo * umna / umna4
        print("  =  " + str(um4))

if znak == '/':
    del0 = int(input("Введите число - "))
    znak = input("Выберите '+','-','*','/' ")
    if znak == '+':
        del1 = int(input("Введите число - "))
        dele = (chislo / del0) + del1
        print("  =  " + str(dele))

    if znak == '-':
        del2 = int(input("Введите число - "))
        dele1 = (chislo / del0) - del2
        print("  =  " + str(dele1))

    if znak == '*':
        del3 = int(input("Введите число - "))
        dele2 = (chislo / del0) * del3
        print("  =  " + str(dele2))

    if znak == '/':
        del4 = int(input("Введите число - "))
        dele3 = chislo / del0 / del4
        print("  =  " + str(dele3))

# else:
#     print('Вы не правильна нажали кнопку !!! ')
