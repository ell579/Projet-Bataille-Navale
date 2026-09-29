class Grille:

    def __init__(self, nombre_lignes, nombre_colonnes):
        self.nombre_lignes = nombre_lignes
        self.nombre_colonnes = nombre_colonnes
        self.vide = '~'
        self.matrice = [self.vide] * (nombre_lignes * nombre_colonnes)

    def tirer(self, ligne, colonne, touche='x'):
        indice = ligne * self.nombre_colonnes + colonne
        self.matrice[indice] = touche

    def ajoute(self, bateau):
        for ligne, colonne in bateau.positions():
            if not (0 <= ligne < self.nombre_lignes and 0 <= colonne < self.nombre_colonnes):
                return

        for ligne, colonne in bateau.positions():
            indice = ligne * self.nombre_colonnes + colonne
            self.matrice[indice] = bateau.marque

        
    def __str__(self):
        texte = ""

        for ligne in range(self.nombre_lignes):
            debut = ligne * self.nombre_colonnes
            fin = debut + self.nombre_colonnes
            texte += "".join(self.matrice[debut:fin]) + "\n"

        return texte.rstrip()