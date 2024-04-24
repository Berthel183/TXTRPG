import random
#from functions import Bonus_Equip



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