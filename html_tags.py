# GROUPE/ Yanis MARTIN, Alexis, Achille


# Fonction fais par Achille
def ouvrir(nom_fichier):
    try:
        # Ouverture du fichier en lecture seulement
        fichier = open(nom_fichier, 'r')
        contenu = fichier.read()
        fichier.close()

        # Traitement de la chaîne pour extraire les tags sans attributs
        tags = []
        tag = ""
        inside_tag = False

        # Parcourir chaque caractère dans la chaîne
        for char in contenu:
            if char == '<':
                inside_tag = True
                tag = '<'
            elif (char == '>') and inside_tag:
                if (' ' in tag):
                    tag = tag.split(' ')[0]
                tag += '>'
                tags.append(tag)
                tag = ""
                inside_tag = False
            elif inside_tag:
                tag += char
        return contenu, tags

    except FileNotFoundError:
        # Gestion de l'erreur si le fichier n'est pas trouvé
        return "Le fichier spécifié est introuvable.", None

# Fonctionfais par Yanis
def verif_chevrons(chaine):
    opening_rafters_counter = 0
    closing_rafters_counter = 0
    last_rafter = ""

    for char in chaine:
        if (char == "<"):
            opening_rafters_counter += 1
        elif (char == ">"):
            closing_rafters_counter += 1

        if (last_rafter == "<" and char == "<"):
            return False
        last_rafter = char

    if opening_rafters_counter != closing_rafters_counter:
        return False

    return True

# Fonction fais par Alexis
def verif_tags(liste):
    pile = []  # Utilisation d'une pile pour suivre l'ordre des balises ouvertes
    for tag in liste:
        if tag[1] != '/':  # Si la balise n'est pas une balise de fermeture
            pile.append(tag)  # Ajoute la balise à la pile
        else:
            # Si la pile est vide, cela signifie qu'il n'y a pas de balise ouverte correspondante
            if len(pile) == 0:
                return False
            # Vérifie si la balise fermante correspond à la dernière balise ouverte
            # Ici on vérifie pour le dernier élément ajouté a la variable stack le charactère d'index 1 jusqu'à la fin, est égale a la chaine entre le caractère 2 (pour éviter le "/") jusqu'à la fin

            if pile[-1][1:] == tag[2:]:
                # Retire la balise ouverte de la pile
                pile.pop()
            else:
                # Si les balises ne correspondent pas, la structure est incorrecte
                return False
    # La structure est correcte si la pile est vide à la fin
    return len(pile) == 0

#Fonction fais par Yanis
def test_html(nom_fic):
    contenu, tags = ouvrir(nom_fic)
    chevrons = ""
    if tags is None:
        return False  # Le fichier n'a pas pu être ouvert correctement

    for char in contenu:
        if (char == "<" or char == ">"):
            chevrons += char

    # L'instruction all permet de vérifier que tout les valeurs itérables dans les parenthèses sont de valeur True
    if verif_chevrons(chevrons):
        return verif_tags(tags)
    else:
        return False  # Les balises ne contiennent pas de chevrons corrects


print(test_html("/Users/achillebosc-pro/Documents/NSI/index.html"))




# Commentaires et combinaison du code (renomer les variables) pour une meilleurs lisibilité du code fais par Achille
