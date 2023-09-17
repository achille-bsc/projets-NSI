def main():
  print("Veuillezchoisir une option")
  print("\n")
  print("(1) - Commencer la partie")
  print("(2) - Voir les règles")


  selection = int(input("Choisir une option\n"))

  match (selection):
    case 1:
      start()
    case 2:
      print_rules()


def start():
  line_break = '\n'
  # Je met line_break*20 pour que la zone d'affichage dans le terminal soit totalement épurrée des print précédents.
  print(line_break*20)
  print('Le jeu commence\n\n')

def print_rules():
  print("Règles du Black Jack")
  print("\n")
  print("Au début du jeu, le croupier reçoit une carte qui est visible, et ne recevra son/ses autre.s cartes qu'une fois le joueur ayant finit de jouer.")
  print("Le joueur reçoit deux cartes, et peut choisir de prendre une autre carte autant de fois qu'il le désir. Son objectif est de s'approcher le plus possible de 21.")
  print("\n")
  print("Les conditions de victoire")
  print("\n")
  print('Au Black Jack vous avez deux façons de gagner, soit vous  faite un "Black Jack" (Vous réunissez un AS et une carte spécial (10, Valet, Dame et Roi)) vous ne perdrezpas votre mise et votre gainsera de 100% de votre mise.')
  print("Soit vous vous rapprochez de 21 plus que le croupier, alors vous ne perdrez pas votre mise et votre gain sera de 50% de votre mise'")
  print("En cas d'égalité avec le croupier, vous ne perdez pas votre mise, mais vous n'avez aucun hain non plus.")
  print("\n")
  exit = str(input("(e) - Revenir au menu principale\n"))
  if (exit == "e"):
    main()

main()