from PIL import Image

im = Image.open(r"Capture d’écran 2024-10-13 à 19.47.31.png")

im.show()


films = ["Retour vers le futur", "Matrix", "Dracula", "Scream", "Saw", "Hook", "Zorro", "Batman", "Avatar", "ET"]

films_trouves = []
score = 0
erreurs = 0
max_erreurs = 3

print("Trouvez les films cachés dans l'image qui apparait. Vous avez le droit a 3 erreurs\n")

while erreurs < max_erreurs and len(films_trouves) < len(films):
    devine = input("Entrez le nom du film : ").lower() 

    if devine in [film.lower() for film in films]:
        if devine in [film.lower() for film in films_trouves]:
            print(f"Vous avez déjà trouvé le film '{devine}'.")
        else:
            films_trouves.append(devine)
            score += 1
            print(f"Bravo ! Vous avez trouvé '{devine}'. Votre score est maintenant de {score} point(s).")
    else:
        erreurs += 1
        print(f"Ce n'est pas le bon film. Vous avez fait {erreurs} erreur(s).")

    print(f"Films trouvés jusqu'à présent : {', '.join(films_trouves)}")
    print(f"Il vous reste {max_erreurs - erreurs} tentative(s).\n")

if erreurs >= max_erreurs:
    print("Vous avez fait 3 erreurs. Vous avez perdu.")
else:
    print(f"Félicitations ! Vous avez trouvé tous les films avec un score de {score} point(s) et seulement {erreurs} erreur(s).")
