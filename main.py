import random

from grille import Grille
from bateau import PorteAvion, Croiseur, Torpilleur, SousMarin

# Création de la grille
grille = Grille(8, 10)

# Création des bateaux
types = [PorteAvion, Croiseur, Torpilleur, SousMarin]
bateaux = []


# Placement aléatoire sans chevauchement
for TypeBateau in types:

    possibilites = []

    for ligne in range(8):
        for colonne in range(10):
            for vertical in [True, False]:

                bateau = TypeBateau(ligne, colonne, vertical)

                valide = True

                for l, c in bateau.positions():

                    # Vérifie que le bateau reste dans la grille
                    if not (0 <= l < 8 and 0 <= c < 10):
                        valide = False
                        break

                    # Vérifie l'absence de chevauchement
                    for autre in bateaux:
                        if (l, c) in autre.positions():
                            valide = False
                            break

                    if not valide:
                        break

                if valide:
                    possibilites.append((ligne, colonne, vertical))

    ligne, colonne, vertical = random.choice(possibilites)

    bateau = TypeBateau(ligne, colonne, vertical)
    bateaux.append(bateau)


coups = 0

while True:

    print(grille)

    ligne = int(input("Ligne : "))
    colonne = int(input("Colonne : "))

    if not (ligne>=0 and colonne>=0 and ligne<8 and colonne<10):
        print("Ce n'est pas sur la grille !")

    else:  
        coups += 1

        touche = False

        for bateau in bateaux:

            if (ligne, colonne) in bateau.positions():

                touche = True

                # Marquer le tir touché
                grille.tirer(ligne, colonne, "💣")

                # Vérifier si toutes les positions du bateau
                # ont été touchées
                coule = True

                for l, c in bateau.positions():

                    indice = l * grille.nombre_colonnes + c

                    if grille.matrice[indice] != "💣":
                        coule = False
                        break

                if coule:

                    # Révéler le bateau coulé
                    for l, c in bateau.positions():
                        indice = l * grille.nombre_colonnes + c
                        grille.matrice[indice] = bateau.marque

                    if isinstance(bateau, PorteAvion):
                        print("🚢 Porte-avions coulé !")

                    elif isinstance(bateau, Croiseur):
                        print("⛴️ Croiseur coulé !")

                    elif isinstance(bateau, Torpilleur):
                        print("⛵ Torpilleur coulé !")

                    elif isinstance(bateau, SousMarin):
                        print("⚓ Sous-marin coulé !")

                else:
                    print("💣 Touché !")

                break

        if not touche:
            grille.tirer(ligne, colonne)
            print("💦 Plouf !")

        # Fin de partie
        tous_coules = True

        for bateau in bateaux:

            for l, c in bateau.positions():

                indice = l * grille.nombre_colonnes + c

                if grille.matrice[indice] != bateau.marque:
                    tous_coules = False
                    break

            if not tous_coules:
                break

        if tous_coules:
            break

print("\nPartie terminée !")
print("Nombre de coups :", coups)