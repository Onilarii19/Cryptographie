def pgcd(a, d):
    while d:
        a, d = d, a % d
    return a

def premier_entre_eux(x,y):
    return pgcd(x, y) == 1

def affine(message, a, b):
    resultat = ""

    for i in message:
        if i.isalpha():
            majuscule = i.isupper()
            i_asciicode = ord(i)
            i_asciicode = (a * (i_asciicode - ord('A' if majuscule else 'a')) + b) % 26
            i_asciicode += ord('A' if majuscule else 'a')
            resultat += chr(i_asciicode)
        else:
            resultat += i

    return resultat
original = input("Entrez le message : ")
a = int (input("Entrez a : "))
while not premier_entre_eux(a,26):
    print(f"{a} n'est pas premier par rapport à 26.")
    a = int(input("Entrez une autre valeur de a: "))
else:
    b = int (input("Entrez b : "))
    chiffre = affine(original, a, b)
    print("Message original:", original)
    print("Message chiffré:", chiffre)









