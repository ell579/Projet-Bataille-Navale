from bateau import Bateau, PorteAvion, Croiseur, Torpilleur, SousMarin
from grille import Grille

def test_init():
    grille = Grille(5, 8)
    assert grille.nombre_colonnes == 8
    assert len(grille.matrice) == 40
    assert grille.matrice == ['~'] * 40


def test_tirer():
    grille = Grille(5, 8)
    grille.tirer(2, 3)
    indice = 2 * 8 + 3
    assert grille.matrice[indice] == 'x'


def test_str():
    grille = Grille(5, 8)
    assert str(grille) == (
        "~~~~~~~~\n"
        "~~~~~~~~\n"
        "~~~~~~~~\n"
        "~~~~~~~~\n"
        "~~~~~~~~"
        )


def test_tirer_affichage():
    grille = Grille(5, 8)
    grille.tirer(2,3)
    assert str(grille) == (
        "~~~~~~~~\n"
        "~~~~~~~~\n"
        "~~~x~~~~\n"
        "~~~~~~~~\n"
        "~~~~~~~~"
        )


def test_init_defaut():
    bateau = Bateau(2, 3)
    assert bateau.ligne == 2
    assert bateau.colonne == 3
    assert bateau.longueur == 1
    assert bateau.vertical == False


def test_positions_horizontales():
    bateau = Bateau(2, 3, longueur=3)
    assert bateau.positions() == [
        (2, 3),
        (2, 4),
        (2, 5)
    ]


def test_positions_verticales():
    bateau = Bateau(2, 3, longueur=3, vertical=True)
    assert bateau.positions() == [
        (2, 3),
        (3, 3),
        (4, 3)
    ]


def test_ajoute():
    grille = Grille(2, 3)
    bateau = Bateau(1, 0, longueur=2)
    grille.ajoute(bateau)
    assert grille.matrice == [
        '~', '~', '~',
        '⛵', '⛵', '~'
    ]


def test_ajoute_hors_grille():
    grille = Grille(2, 3)
    bateau = Bateau(1, 0, longueur=4)
    grille.ajoute(bateau)
    assert grille.matrice == [
        '~', '~', '~',
        '~', '~', '~'
    ]


def test_coule():
    grille = Grille(5, 8)
    bateau = Bateau(2, 3, longueur=3)
    grille.tirer(2, 3)
    grille.tirer(2, 4)
    grille.tirer(2, 5)
    assert bateau.coule(grille)


def test_pas_coule():
    grille = Grille(5, 8)
    bateau = Bateau(2, 3, longueur=3)
    grille.tirer(2, 3)
    grille.tirer(2, 4)
    assert not bateau.coule(grille)




def test_porte_avion():
    g = Grille(5, 10)
    b = PorteAvion(1, 2)
    g.ajoute(b)
    assert g.matrice[12:16] == ['🚢', '🚢', '🚢', '🚢']


def test_croiseur():
    b = Croiseur(0, 0)
    assert b.longueur == 3


def test_torpilleur():
    b = Torpilleur(0, 0)
    assert b.longueur == 2


def test_sous_marin():
    b = SousMarin(0, 0)
    assert b.longueur == 2
