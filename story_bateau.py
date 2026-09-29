from bateau import Bateau

# Cas où les bateaux se chevauchent

b1 = Bateau(2, 3, longueur=3)
b2 = Bateau(2, 5, longueur=2)

chevauchement = False

for position in b1.positions():
    if position in b2.positions():
        chevauchement = True

print("Chevauchement :", chevauchement)


# Cas où les bateaux ne se chevauchent pas

b3 = Bateau(0, 0, longueur=3)
b4 = Bateau(4, 4, longueur=2)

chevauchement = False

for position in b3.positions():
    if position in b4.positions():
        chevauchement = True

print("Chevauchement :", chevauchement)