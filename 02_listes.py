print("\n")

eleves = ["Thomas", "Lisa", "Helene", "Patrick", "Paul"]
print(eleves)

notes = [10.5, 12.0, 16.0, 17.5, 4.0]
print(notes)

dates = []

print(notes[0])
print(notes[len(notes)-1])
print(notes[-1])
print(notes[-5])
print(notes[len(notes) * -1])

eleves.append("Lucas")
notes.append(20.0)

print(eleves)
print(notes)

eleves.remove("Lucas")
eleves.pop(3)

jours = ["lun", "mar", "mer", "jeu", "ven", "sam", "dim"]
lun_ven = [jours[0], jours[1], jours[2]]

lun_ven = jours[0:5]

print(lun_ven)

wk = jours[5:]

print(wk)

print(jours[:5])
print(jours[-2:])

jours_fr_en = [
    ["lun", "mar", "mer", "jeu", "ven", "sam", "dim"],
    ["mon","tue", "wed", "thu", "fri", "sat", "sun"]
]

print(jours_fr_en[1][5:])

image = [
    [[12,125,255], ".", ".", ".", ".",".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".",".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".",".", ".", ".", ".", "."]
]