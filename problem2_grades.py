etudiant = [
    ("Ali" , 12),
    ("Fatou" , 17),
    ("Moussa" , 9),
    ("Awa" , 14),
    ("Ibrahima", 7)
]
prenom = input("enter votre prenom :")
note = float(input("entrer votre note"))
def afficherEtudiant(liste):
    print("etudiant :  %s "prenom" ,  " + " , "note"  %f")
    return etudiant

etudiant = [
    ("Ali" , 12),
    ("Fatou" , 17),
    ("Moussa" , 9),
    ("Awa" , 14),
    ("Ibrahima", 7)
]
note = float(input("entrer votre note :"))
def analyserListe(liste):
    total = sum(liste)
    moyenne = total / len(liste)
    maximumNote = note[0]git
    minimumNote = note[0]
    for n in note:
        if note > maximumNote:
        maximumNote = n

        if note < minimumNote:
        minimumNote = n

    return moyenne, maximumNote, minimumNote
note = [12, 20, 15, 17]



students = [
    ("Ali" , 12),
    ("Fatou" , 17),
    ("Moussa" , 9),
    ("Awa" , 14),
    ("Ibrahima", 7)
]
listeAdmis = []
listeAjourne = []
etudiant = input("entrer un etudiant :")
for i in students:
    if note >= 10:
        listeAdmis.append(etudiant)
    else:
        listeAjourne.append(etudiant)



    





