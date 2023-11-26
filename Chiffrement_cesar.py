msg = input("Entrez le message à chiffrer : ")
decalage = int(input("Entrez le décalage souhaité : "))

def encodage(msg, decalage):
    chiffre = ""
    for i in msg:
        if i.isalpha():
            majuscule = i.isupper()
            i_asciicode = ord(i)
            i_asciicode = (i_asciicode - ord('A' if majuscule else 'a') + decalage) % 26 + ord('A' if majuscule else 'a')
            chiffre += chr(i_asciicode)
        else:
            chiffre += i
    return chiffre

resultat = encodage(msg, decalage)

print("Message original : ", msg)
print("Message chiffré : ",resultat)