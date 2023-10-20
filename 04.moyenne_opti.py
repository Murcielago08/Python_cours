print("\n")

note = 0
moyenne = 0
div_sans_0 = 0
choix = "o"

notes = []

while choix == "o":
    note = float(input("Saisissez une note: "))
    if (note < 0 or note > 20):
        print(f"Entrer une note entre 0 et 20 s'il vous plaît")

    if (note != 0 ):
        div_sans_0 += 1 

    
    moyenne += note
    notes.append(note)

    choix = input("Voulez-vous saisir une nouvelle note ? (o/n)")

    if (choix != "o" or choix != "n"):
        print(f"Entrer un 'o' ou un 'n' s'il vous plaît")

print(f"Moyenne de la classe: {round(moyenne / len(notes), 2)}")
print(f"Moyenne optimisée de la classe: {round(moyenne / div_sans_0, 2)}")
