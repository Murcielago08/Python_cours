date = "26/07/2003"

jour = int(date[:2]) 
mois = int(date[3:5])
annee = int(date[6:])

print(date[:2] + "." + date[3:5] + "." + date[6:])

print(date.replace("/", "."))

print(jour, mois, annee, sep=".")

result = f"La date est : {jour}.{mois}.{annee}"
print(result)

habitant = 7_753_000_000
superficie = 149_000_000

print(f"Nb habitant par km² : {round(habitant / superficie, 2)}")