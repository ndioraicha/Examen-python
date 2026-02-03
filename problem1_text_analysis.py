def analyserPhrase(liste):
    phrase = input("entrer une phrase :")
    phraseCon = phrase.casefold()
    phraseDec = phrase.split
    print("conversion : ", phraseCon)

    print("phrase découpée : ", phraseDec)
    return phraseCon, phraseDec
phrases = ["bonjour les etudiant", "coucou les professeurs", "bonsoir maman"]

phrase = input("entrer une phrase :")
totalMot = 0
maximumLen  = phrase[0]
voyelle = "aeiouy"
compteur1 = [0]
compteur2 = [0]
for i in phrase.casefold():
    for mot in phrase:
        compteur1 += i
        totalMot = compteur1
        print("nombre de mots : ", totalMot)

    if len(mot) > maximumLen:
        maximumLen = len(mot)

for lettre in phrase.casefold():
    if lettre in  voyelle:
        compteur2 += 1

    print("le nombre total de voyelle : ", compteur2)   

nouvellePhrase = input("entrer une nouvelle phrase :")
for mot in phrase.casefold():
    if len(mot) % 2 == 0:
        print("mot : " , mot.upper())
    else:
        print("mot : " , mot)


