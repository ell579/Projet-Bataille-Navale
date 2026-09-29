from grille import Grille

grille = Grille(5, 8)        #création de la grille

while True:
    print(grille)      #affichage de la grille

    ligne = int(input("ligne = "))          #demande de saisir une ligne
    colonne = int(input("colonne = "))          #demande de saisir une colonne

    grille.tirer(ligne, colonne)              #tire sur l'endroit indiqué
    #retour à l'étape 2