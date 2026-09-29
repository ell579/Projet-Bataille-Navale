class Bateau:

    def __init__(self, ligne, colonne, longueur=1, vertical=False):
        self.ligne = ligne
        self.colonne = colonne
        self.longueur = longueur
        self.vertical = vertical
        self.marque = '⛵'

    def positions(self):
        positions = []

        for i in range(self.longueur):
            if self.vertical:
                positions.append((self.ligne + i, self.colonne))
            else:
                positions.append((self.ligne, self.colonne + i))

        return positions

    def coule(self, grille):
        for ligne, colonne in self.positions():
            indice = ligne * grille.nombre_colonnes + colonne

            if grille.matrice[indice] != 'x':
                return False

        return True


class PorteAvion(Bateau):

    def __init__(self, ligne, colonne, vertical=False):
        super().__init__(ligne, colonne, 4, vertical)
        self.marque = '🚢'


class Croiseur(Bateau):

    def __init__(self, ligne, colonne, vertical=False):
        super().__init__(ligne, colonne, 3, vertical)
        self.marque = '⛴'


class Torpilleur(Bateau):

    def __init__(self, ligne, colonne, vertical=False):
        super().__init__(ligne, colonne, 2, vertical)
        self.marque = '🚣'


class SousMarin(Bateau):

    def __init__(self, ligne, colonne, vertical=False):
        super().__init__(ligne, colonne, 2, vertical)
        self.marque = '🐟'