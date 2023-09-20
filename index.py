import random


def create_card(card: list):
    new_card: tuple = ()
    symbole = random.randint(1, 4)
    number = random.randint(1, 13)
    for card in card:
        while (card[0] == symbole and card[1] == number):
            symbole = random.randint(1, 4)
            number = random.randint(1, 13)
    return (symbole, number)


# le deck sera une liste de tuple ----> [(1, 3), (3, 5)]
def analyze_deck(deck) -> list:
    analized_cards = []
    for card in deck:
        symbole = card[0]
        match symbole:
            case 1:
                symbole = "carreau"
            case 2:
                symbole = "coeur"
            case 3:
                symbole = "pic"
            case 4:
                symbole = "trefle"

        number = str(card[1])
        match number:
            case "11":
                number = "Valet"
            case "12":
                number = "Dame"
            case "13":
                number = "Roi"
            case "1":
                number = "As"

        analized_cards.append(str(number) + " de " + symbole)
    return analized_cards


def calculate_total_values(deck: list, player_value: int) -> int:
    new_player_value = 0
    for card in deck:
        if (card[1] == 1 and player_value < 11):
            new_player_value += 11
        else:
            new_player_value += int(card[1])
    return new_player_value


def get_total_card(dealer_cards, player_cards) -> list:
    total_cards = []
    for dealer_card in dealer_cards:
        total_cards.append(dealer_card)
    for player_card in player_cards:
        total_cards.append(player_card)
    return total_cards


def print_datas(dealer_cards_analyzed: list, player_cards_analyzed: list, player_value: int):
    print("La carte du croupier est:")
    print(dealer_cards_analyzed[0] + "\n\nVos cartes sont les suivantes")
    for player_card in player_cards_analyzed:
        print(player_card)

    print("Vous avez %i point" % player_value)


def select_winner(player_value, dealer_value):
    if (player_value > dealer_value and player_value <= 21):
        print("Félicitation vous avez gagné la partie")
    elif ((player_value > 21 and dealer_value > 21) or player_value == dealer_value):
        print("C'est une égalité !! vous finissez tout les deux avec %i points" %
              player_value)
    elif (player_value == 21):
        print("Félicitation vous avez-fait un black-jack")
    else:
        print("Dommage, vous avez perdu !")


def ask_question(player_cards, dealer_cards, dealer_cards_analyzed, player_cards_analyzed, player_value, dealer_value, total_cards):
    player_choice = str(input('Voullez-vous "hit" ou "stand" ?'))

    if player_choice == "hit":
        player_cards.append(create_card(total_cards))
        total_cards = get_total_card(dealer_cards, player_cards)

        print_datas(dealer_cards_analyzed, player_cards_analyzed, player_value)
    else:
        select_winner(player_value, dealer_value)


def main():
    print("Le jeu commence:\n")
    dealer_cards = []
    player_cards = []
    player_value = 0
    dealer_value = 0

    total_cards = get_total_card(dealer_cards, player_cards)

    for card in range(2):
        dealer_cards.append(create_card(total_cards))
        total_cards = get_total_card(dealer_cards, player_cards)

    for card in range(2):
        player_cards.append(create_card(total_cards))
        total_cards = get_total_card(dealer_cards, player_cards)

    dealer_value = calculate_total_values(dealer_cards, dealer_value)
    player_value = calculate_total_values(player_cards, player_value)

    dealer_cards_analyzed = analyze_deck(dealer_cards)
    player_cards_analyzed = analyze_deck(player_cards)

    print_datas(dealer_cards_analyzed, player_cards_analyzed, player_value)

    ask_question(player_cards, dealer_cards, dealer_cards_analyzed,
                 player_cards_analyzed, player_value, dealer_value, total_cards)


main()
