#1.Suma numerelor de la 1 la 100
def suma_1_100():
    suma = sum(range(1, 101))
    return suma

#2.Afisarea primelor 20 de numere impare
def primele_20_impare():
    impare = [i for i in range (1, 40, 2)]
    return impare

#3.Cel mai mare divizor comun pentru 2 numere citite de la tastatura
import math
def divizor_2_numere():
    a = int(input("Introduceți primul număr: "))
    b = int(input("Introduceți al doilea număr: "))
    return math.gcd(a, b)

#4.Afisati daca un numar citit de la tastatura este prim
def prim():
    num = int(input("Introduceți un număr: "))
    if num < 2:
        return True
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

#5.Afisati suma si media unei liste de numere citite de la tastatura
def suma_media():
    nr1 = int(input("Introduceți primul număr: "))
    nr2 = int(input("Introduceți al doilea număr: "))
    suma = nr1 + nr2
    media = suma / 2
    return suma, media


#6.Se citesc 3 numere de la tastatura, verificati daca acestea pot reprezenta unghiurile unui triunghi
def triunghi():
    a = int(input("Introduceți primul unghi: "))
    b = int(input("Introduceți al doilea unghi: "))
    c = int(input("Introduceți al treilea unghi: "))
    return a + b + c == 180 and a > 0 and b > 0 and c > 0

#7. Sortati o lista de elemente citite de la tastatura, folosind orice metoda de sortare doriti (nu functia sort)
def metoda_bulelor():
    numere = list(map(int, input("Introduceți numerele, separate prin spațiu: ").split()))
    n = len(numere)
    for i in range(n):
        for j in range(0, n - i - 1):
            if numere[j] > numere[j + 1]:
                numere[j], numere[j + 1] = numere[j + 1], numere[j]
    return numere

#8. Scrieti un program care afiseaza ziua saptamanii pentru un numar citit de la tastatura (de la 1 la 7) unde  1=luni , 7 = duminica
def zilele_săptămânii():
    zile = ["Luni", "Marți", "Miercuri", "Joi", "Vineri", "Sâmbătă", "Duminică"]
    zi_număr = int(input("Introduceți un număr de la 1 la 7: "))
    if 1 <= zi_număr <= 7:
        return zile[zi_număr - 1]
    else:
        return "Număr invalid"

#9.Afisati maximul dintr-un vector de elemente citit de la tastatura
def număr_max():
    numere = list(map(int, input("Introduceți numerele, separate prin spațiu: ").split()))
    return max(numere)

#10. Rezolvati ecuatia de gradul al doilea
def ecuație():
    a = float(input("Introduceți coeficientul a: "))
    b = float(input("Introduceți coeficientul b: "))
    c = float(input("Introduceți coeficientul c: "))

    discriminant = b**2 - 4*a*c

    if discriminant > 0:
        root1 = (-b + discriminant**0.5) / (2*a)
        root2 = (-b - discriminant**0.5) / (2*a)
        print("Ecuația are două soluții reale:", root1, "și", root2)
    elif discriminant == 0:
        root = -b / (2*a)
        print("Ecuația are o soluție dublă:", root)
    else:
        print("Ecuația nu are soluții reale.")

#ecuație()

print("Maximul este:", număr_max())

#print(zilele_săptămânii())

#print(metoda_bulelor())

#print("Unghiurile pot forma un triunghi?", triunghi())

#suma, media = suma_media()
#print("Suma:", suma)

#print("Media:", media)

#print("Numărul este prim?" , prim())

#print(divizor_2_numere())

#print(primele_20_impare())

#print(suma_1_100())