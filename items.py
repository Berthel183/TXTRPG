import random
#from functions import Bonus_Equip
from functions import Weapon


print("scegli un'arma!")




weapon_item_tier_1 = {'Spada':5,'Claymore':10} #danno aumentato
armor_item_tier_1 = {'Cotta di maglia':15,'Armatura a piastre':30} #hp max
shield_item_tier_1 = {'buckler':4,'Scudo a torre':15} #riduzione danni

weapon = (weapon_item_tier_1)
print(weapon)
armor = None
shield = None

def item_drops():
    drop = weapon_item_tier_1
    
arma = Weapon('','',0) #richiamare gli attributi
arma.atk_bonus = 5 

#Chiamare il file ITEMS.PY e dentro ficcare tutte le classi dell'equip, padre e figli Equip>Weapon>Sword---'machete/katana', dare propietà a weapon/armor/shield e lavrorare solo su queste, non su Equip(non va toccato o bay si arrabbia)