import random


def create_card(cards: list):
    # Permet de déterminer le symbole de la carte (Carreau, coeur, pic, trefle)
    symbole = random.randint(1, 4)
    # permet de déterminer la valeur de la carte (As, 2, 3, 4, 5, 6, 7, 8, 9, 10, Valet, Dame, Roi)
    number = random.randint(1, 13)

    # On vérifie (grâce a la variable card qui contitent toutes les cartes en jeux) que la carte que l'on génère ne contient pas de doublons
    for card in cards:
        # Tant que l'on génère une carte doublons, on regénère la carte
        while (card[0] == symbole and card[1] == number):
            symbole = random.randint(1, 4)
            number = random.randint(1, 13)
    # On renvoit un Tuple qui représente la carte ---> (Symbole, Valeur)
    return (symbole, number)


# le deck sera une liste de tuple ----> [(1, 3), (3, 5)]
# La fonction servira donc a transformer des données brutes en données lisibles, exemple ---> [(1, 1), (3, 12)] sera transformé en ["As de Carreau", "Dame de Pic"]
# Lors de la déclaration de la  fonction, on peutvoir un       -> list       qui permet de spécifier que la fonction renverra  exclusivement une list
# Typer ses variables et ses fonction permet de prévenir certaines erreur lorsque l'on travaille sur un code complexe, cela permet donc de gagner du temps
def analyze_deck(deck) -> list:
    # on renverra la variable analized_cards qui sera une liste de toutes les données transformées en données lisible
    analized_cards = []

    # Pour chaque carte, on applique le code suivant
    for card in deck:
        # Le symbole de la carte est stocké dans la première valeur de mon tuple
        symbole = card[0]
        # L'opérateur match case est utilisé pour faire une même condition a répétition
        # On va comparer la valeur contenu dans la variable symbole avec les valeurs indéquées après chaque case
        match symbole:
            # Ici, on compare la valeur 1 avec la valeur contenu dans la variable symbole
            # Si les deux valeurs sont identique on éxécute le code correspondant
            # Sinon on passe a la valeur case suivante
            case 1:
                symbole = "Carreau"
            case 2:
                symbole = "Coeur"
            case 3:
                symbole = "Pic"
            case 4:
                symbole = "Trefle"
        # La variable number va contenir la valeur de la carte qui est stockée dans le deuxième élément du tuple
        # On utilise str() pour que la variable number soit déclarée comme étant de  type string (ou str), c'est assez utile pour avoir une bonne auto-complétion sur certains éditeurs de code
        number = str(card[1])

        # Le match case est réutilisé ici pour la même raison que précédement
        match number:
            case "11":
                number = "Valet"
            case "12":
                number = "Dame"
            case "13":
                number = "Roi"
            case "1":
                number = "As"
        # On ajoutes nos données sous forme de string a la variable analized_cards afin de pouvoir  réutiliser des chaines de caractères toutes prête lorque l'on en aura besoin
        analized_cards.append(number + " de " + symbole)
    # On renvoit nos carte sous forme de données lisible pour l'utilisateur
    return analized_cards

# Cette fonction permet de calculer la valeur total d'une main


def calculate_total_values(deck: list) -> int:
    # La variable new_player_value va stocker le score que l'on est en train de calculer
    new_player_value = 0

    # Pour chaque carte de la main
    for card in deck:
        # Si c'est un As et que le score est inférieur a 11 (car si le score est suppérieur a 11, on ne peut pas ajouter le 11 que vaudrais l'As)
        if (card[1] == 1 and new_player_value < 11):
            # On ajoute 11 au score du joueur
            new_player_value += 11
        # Si la carte est une carte spéciale, on ajoute 10 au score
        elif (card[1] > 10):
            new_player_value += 10
        # Si la carte est une carte normale ou que c'est un as qui ne peut valoire que 1, on ajoute la valeur adéquate a la variable new_player_value
        else:
            new_player_value += int(card[1])
    # On renvoit le score total
    return new_player_value

# Cette fonction permet de réunir toutes les cartes dans une seule liste, afin que la génération de carte ne puisse pas générer de doublons
# On a typé cette variable également pour s'assurer de renvoyer une liste et avoir une meilleure auto-complétion


def get_total_card(dealer_cards, player_cards) -> list:
    # La variable total_cards est celle qui va stocker toutes les cartes en jeu avant de les return
    total_cards = []
    # On copie chaque carte du dealer et chaque carte du joueur dans la variable total_cards
    for dealer_card in dealer_cards:
        total_cards.append(dealer_card)
    for player_card in player_cards:
        total_cards.append(player_card)
    # On renvoit la liste de toutes les cartes
    return total_cards

# Cette fonction permet d'envoyer dans la console toutes les informations visibles par le joueur


def print_datas(dealer_cards_analyzed: list, player_cards_analyzed: list, player_value: int):
    # Permet de sauter des lignes afin de mettre en évidence les informations dernièrement écrites dans la console
    print('\n\n\n\n\n')
    # Dans ce print, on utilise l'opérateur %s qui permet d'écrire une chaine de caractère dans une autre en écrivant          % ma_variable          après la chaine de  caractère
    print("La première carte du croupier est:\n%s" % dealer_cards_analyzed[0])
    print("\nVos cartes sont les suivantes:")
    # On écrit les cartes de l'utilisateur dans la console
    for player_card in player_cards_analyzed:
        print(player_card)
    # Dans ce print, on utilise l'opérateur %i qui permet d'écrire une valeur int dans une string en écrivant          % ma_variable          après la chaine de  caractère
    print("Vous avez %i points" % player_value)

# La fonction select_winner permet de calculer le gagnant en fonction des points du joueurs et de ceux du croupier
# Ici on peut voir que le paramètre dealer_card qui comporte le typage (avec dealer_cards: str) qui me permetde diminuer le taux d'erreur possible lorsde l'utilisation de la fonction et permet également une meilleure auto-complétion


def select_winner(player_value, dealer_value, dealer_cards: str):
    # Si le joueur a plus que le croupier et que son score est inférieur a 21, on affiche sa victoire ainsi que les point et les cartes du croupier
    if (player_value > dealer_value and player_value < 21):
        print("Félicitation vous avez gagné la partie !\n!")
        print("Le croupier  avait %i points avec les cartes suivants:" %
              dealer_value)
        for card in dealer_cards:
            print(card)
    # Si le croupier et le joueur ont le même score, ou qu'ils ont un score suppérieur a 21, on déclare l'égalité
    elif ((player_value > 21 and dealer_value > 21) or (player_value == dealer_value)):
        print("C'est une égalité !! vous finissez tout les deux au dessus de 21, ou avec avec %i points" %
              player_value)
    # Si le joueur a fait un blackJack, il a forcément gagné car la possibilité d'égalité a déjà été géré précédement
    elif (player_value == 21):
        print("Félicitation vous avez-fait un black-jack !")
    # Si le dealer a plus de 21 points, il a perdu et le joueur gagne par défaut !
    elif (dealer_value > 21 and player_value <= 21):
        print("Félicitation, vous avez gagné car le croupier a %i points" %
              dealer_value)
        for card in dealer_cards:
            print(card)
    # Dans tout les autres cas de figure le joueur a perdu, on affiche alors la défaite du joueur ainsi que les points et les cartes du croupier
    else:
        print("Dommage, vous avez perdu !")
        print("Le croupier  avait %i points avec les cartes suivants:" %
              dealer_value)
        for card in dealer_cards:
            print(card)

# La fonction main est la fonction principale du programme qui se charge du bon déroulement d'un tour de jeu


def main(pick_cards=True, dealer_cards=[], player_cards=[], player_score=0, dealer_score=0, total_cards=[]):
    # Si le paramètre pick_cards vaut True, on déclare les variables qui stockent les cartes et les scores pour le croupier et pour le joueur
    if (pick_cards):
        print("Le jeu commence:\n")
        dealer_cards = []
        player_cards = []
        dealer_score = 0
        player_score = 0
        # La variable total_cards permet  de stocker la totalité des cartes en jeu
        total_cards = []

        # On génère ici 2 carte pour le croupier, deux cartes pour le joueur, et on stock le tout dans les variables correspondantent ainsi que dans la variable total_cards
        for card in range(2):
            dealer_cards.append(create_card(total_cards))
            player_cards.append(create_card(total_cards))

            total_cards = get_total_card(dealer_cards, player_cards)
    # On calcule le scoredes deux joueurs (le croupier, et le joueur)
    dealer_score = calculate_total_values(dealer_cards)
    player_score = calculate_total_values(player_cards)

    # Ici on récupère les  chaines de caractères qui vont permettre d'afficher les cartes du joueur et la première carte du croupier
    dealer_cards_analyzed = analyze_deck(dealer_cards)
    player_cards_analyzed = analyze_deck(player_cards)

    # On utilise la fonction print_datas() qui permet d'écrire dans la console les informations auxquelles le joueur peut avoir accès
    print_datas(dealer_cards_analyzed, player_cards_analyzed, player_score)

    # Ici on demande a l'utilisateur si il souhaite "hit" (Demander une nouvelle carte) ou "stand" (En rester la et voir les résultats)
    # Il y a \n a la fin car sur des éditeurs autre que EduPython, les input doivent être rentrées dans la console au lieu d'une fenêtre extérieure
    player_choice = str(input('Voullez-vous "hit" ou "stand" ?\n'))

    # Si le joueur souhaite "hit", on lui génère une carte, on l'ajoute a ses carte ainsi qu'aux cartes actuellement en jeu, et on relance la fonction main() utilisant ainsi le principe de récusivité
    if player_choice == "hit":
        player_cards.append(create_card(total_cards))
        total_cards = get_total_card(dealer_cards, player_cards)

        main(False, dealer_cards, player_cards,
             player_score, dealer_score, total_cards)
    # Si l'utilisateur choisit de "stand" ou  qu'il écrit autre chose, on utilise la fonction select_winner qui permet de déterminer puis d'afficher la victoire ou la défaite
    else:
        # Tant que le croupier n'est pas a 16 points minimum, il pioche une autre carte
        while dealer_score < 16:
            dealer_cards.append(create_card(total_cards))
            total_cards = get_total_card(dealer_cards, player_cards)
            dealer_score = calculate_total_values(dealer_cards)
        select_winner(player_score, dealer_score, dealer_cards_analyzed)

main()