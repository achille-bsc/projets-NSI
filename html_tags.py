# Variables Globales
max_group_size = 3

# -----------------
# | Code de Yanis |
# -----------------
class Chambre:
  def __init__(self, number: int, floor: int, capacity: int, clear_state: bool, occupation_state: bool, view: int):
    self.number = number
    self.floor = floor
    self.capacity = capacity
    self.is_clear = clear_state
    self.occupation_state = occupation_state
    self.view = view
    self.pricing = 0
    
    match self.view:
      case 0:
        self.pricing += 10
      case 1:
        self.pricing += 20
      case 2:
        self.pricing += 30
      case 3:
        self.pricing += 40
      case 4:
        self.pricing += 50

    self.pricing += floor*25
    self.pricing += (capacity*((self.pricing/100)*60))
      
      
  def nettoyer(self):
    '''permet de nettoyer la chambre'''
    if self.is_clear:
      return True
    else:
      self.is_clear = True
    return self.is_clear
  def prendre(self):
    '''le client reserve la chambre'''
    if self.occupation_state:
      return -1
    else:
      self.occupation_state = True
    return self.occupation_state
  def liberer(self):
    '''le client libère la chambre'''
    self.occupation_state = False
    return True
  def payer(self):
    '''la solde du client est déduite du montant de la chambre'''
    print("Il faut payer le tarif pour vous sera de ", self.pricing)

# -------------------
# | Code de Achille |
# -------------------

class Hotel():
  # TODO: Ajouter le type du paramètre bedroom
  def __init__(self, nom: str, ville: str, adresse: str, etages: int, piscines: bool) -> None:
    self.nom = nom
    self.ville = ville
    self.adresse = adresse
    self.etages = etages
    etage: list[Chambre] = []
    self.chambres = [etage for i in range(etages)]
    self.piscine = piscines
    
  def ajouter_chambre(self, chambre: Chambre):
    etage = chambre.floor
    if (len(self.chambres[etage]) == 0):
      self.chambres[etage] = [chambre]
    else:
      self.chambres[etage].append(chambre)

    if (self.piscine):
      chambre.pricing += 15

    return self.chambres
  
  def get_dispo(self):
    nb_free_bedrooms = 0
    
    for bedroom in self.chambres:
      if bedroom.is_free():
        nb_free_bedrooms += 1
        
    return nb_free_bedrooms
  
  def netoyer(self):
    for bedroom in self.chambres:
      bedroom.nettoyer()
  
  def get_name(self):
    return self.nom
  def get_ville(self):
    return self.ville
  def get_adresse(self):
    return self.adresse
  def get_chambres(self):
    return self.chambres
  def get_piscine(self):
    return self.piscine
  

class Client():
  def __init__(self, argent, size, nom) -> None:
    self.argent = argent
    self.goupe_size = size
    self.nom = nom
    
  def search_rooms_by_price(self, hotel: Hotel, price: float):
    possible_rooms = []
    for etage in hotel.chambres:
      for chambre in etage:
        if (chambre.pricing <= price):
          possible_rooms.append(chambre)

    possible_rooms.sort(key=lambda x: x.pricing)
    return possible_rooms
  


# ------------------------
# | Fonction d'affichage |
# ------------------------

def view_transformer(view: int | str):
  if (type(view) is int):
    match view:
      case 0:
        return "Vue sur mer"
      case 1:
        return "Vue sur montagne"
      case 2:
        return "Vue sur Canyon"
      case _:
        return "Aucune vue"
  else:
    match view:
      case "Vue sur mer":
        return 0
      case "Vue sur montagne":
        return 1
      case "Vue sur Canyon":
        return 2
      case _:
        return -1


def display_possible_rooms(rooms: list[Chambre]):
  display_string = ""

  for room in rooms:
    display_string += "    - Chambre n°%i: %i€, %i Personnes, %s, Étage n°%i\n" % (room.number, room.pricing, room.capacity, view_transformer(room.view), room.floor)
  
  return display_string

def create_hotel(floors, rooms_by_floor):
  hotel = Hotel("Hotel", "Ville de l'Hotel", "1 rue de l'Hotel", 5, True)
  for floor in range(floors):
    for room in range(rooms_by_floor):
      hotel.ajouter_chambre(Chambre(((floor+1)*100 + room + 1), floor, 5, True, False, 0))
  
  return hotel

def main():
  hotel = create_hotel(3, 5)
  money = float(input("Quelle est votre limite monaitaire ?\n"))
  group_size = int(input("Combien de personnes êtes-vous ?\n"))
  if group_size > max_group_size:
    print("Notre hotel ne contient aucune chambre de plus de %i personnes\n" % max_group_size)
    choice = str(input("Souhaitez-vous continuer la recherche en diminuant les effectifs ? (o/n)\n"))

    if (choice in ["o", "oui", "y", "yes"]):
      return main()
    else: return
  name = str(input("Veuillez rensseigner un nom de Groupe (Nom de famille par exemple)\n"))

  client = Client(money, group_size, name)


  print("Voici les hotels trouvés:\n%s" % display_possible_rooms(client.search_rooms_by_price(hotel, money)))


main()
