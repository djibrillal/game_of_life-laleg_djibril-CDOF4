import time
import random

def generer_grille_aleatoire(hauteur, largeur):
    """
    Génère une grille de taille (hauteur x largeur)
    avec des cellules vivantes ou mortes de manière aléatoire.
    """
    return [
        [random.choice([0, 1]) for _ in range(largeur)]
        for _ in range(hauteur)
    ]

def afficher_grille(grille):
    """
    Affiche la grille dans la console.
    Utilise '#' pour les cellules vivantes et ' ' pour les cellules mortes.
    """
    for ligne in grille:
        print("".join('#' if cellule == 1 else ' ' for cellule in ligne))
    print()

def compter_voisins_vivants(grille, x, y):
    """
    Compte le nombre de cellules voisines vivantes autour de la cellule (x, y).
    On considère ici les 8 voisins (haut, bas, gauche, droite, diagonales).
    """
    voisins = 0
    hauteur = len(grille)
    largeur = len(grille[0])
    
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue  # On ne compte pas la cellule elle-même
            nx, ny = x + dx, y + dy
            
            # Vérifie si (nx, ny) est bien dans la grille
            if 0 <= nx < hauteur and 0 <= ny < largeur:
                voisins += grille[nx][ny]
    
    return voisins

def prochaine_generation(grille):
    """
    Calcule la grille suivante selon les règles du Game of Life :
      - Une cellule vivante meurt si elle a moins de 2 voisins vivants (sous-population)
        ou si elle a plus de 3 voisins vivants (surpopulation).
      - Une cellule morte devient vivante si elle a exactement 3 voisins vivants (reproduction).
    """
    hauteur = len(grille)
    largeur = len(grille[0])
    
    nouvelle_grille = [[0]*largeur for _ in range(hauteur)]
    
    for x in range(hauteur):
        for y in range(largeur):
            voisins_vivants = compter_voisins_vivants(grille, x, y)
            cellule_actuelle = grille[x][y]
            
            if cellule_actuelle == 1:
                # Règle 1 et 3 : survit si 2 ou 3 voisins, sinon meurt
                if voisins_vivants == 2 or voisins_vivants == 3:
                    nouvelle_grille[x][y] = 1
                else:
                    nouvelle_grille[x][y] = 0
            else:
                # Règle 4 : une cellule morte devient vivante si elle a 3 voisins vivants
                if voisins_vivants == 3:
                    nouvelle_grille[x][y] = 1
    
    return nouvelle_grille

def est_stable(grille, nouvelle_grille):
    return grille == nouvelle_grille

def main():
    # Demander la taille de la grille à l'utilisateur
    try:
        hauteur = int(input("Entrez la hauteur de la grille (par défaut 20) : ") or 20)
        largeur = int(input("Entrez la largeur de la grille (par défaut 20) : ") or 20)
        if hauteur <= 0 or largeur <= 0:
            raise ValueError("Les dimensions doivent être des nombres positifs.")
    except ValueError as e:
        print(f"Entrée invalide : {e}. Utilisation des dimensions par défaut (20x20).")
        hauteur, largeur = 20, 20

    grille = generer_grille_aleatoire(hauteur, largeur)
    
    while True:
        afficher_grille(grille)
        nouvelle_grille = prochaine_generation(grille)
        if est_stable(grille, nouvelle_grille):
            print("La grille est stable. Fin de la simulation.")
            break
        grille = nouvelle_grille
        time.sleep(0.2)

if __name__ == "__main__":
    main()

