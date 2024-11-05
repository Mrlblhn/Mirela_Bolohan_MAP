def verificare_numere():
    if 10 > 20:
        print("Este mai mare")
    else:
        print("Nu este mai mare")


def tipuri_de_date():
    x=int(3)
    y="MAP"
    print(type(x))
    print(type(y))


def tuplu():
    masini=["Audi","BMW","Dacia"]
    x,y,z = masini
    print (x)
    print (y)
    print (z)


def interpolare():
    varsta = 212
    text = "Numele meu este Alex si am {} de ani"
    print (text.format(varsta))


def instructiunea_while():
    i = 1
    while i <= 5:
        print("Bucla while", i)
        i+=1

def lista_elemente():
    elemente=[]
    n = int(input("Introdu numarul de elemente"))
    for i in range (0,n):
        print("Introdu elementul pentru pozitia ",i)
        item=int(input())
        elemente.append(item)
    print("Lista este ", elemente)

#lista_elemente()
#verificare_numere()
#tipuri_de_date()
#tuplu()
#interpolare()
#instructiunea_while()