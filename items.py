class Equip:
    def __init__(self,equip_name,equip_type):
        self.equip_name = equip_name
        self.equip_type = equip_type

class Weapon(Equip):
    def __init__ (self,equip_name,equip_type,atk_bonus): #sempre riportare le proprietà del genitore
        super().__init__(equip_name,equip_type)
        self.atk_bonus = atk_bonus #puoi specificare int con : int, non necessario
        

class Helm(Equip):
    pass

class Shield(Equip):
    pass

class Chest(Equip):
    pass



arma = Weapon('','',0)  #istanziamento della classe

weapon_item_tier_1 = {
    0:{'nome':'Spada','tipo':'Arma','danno':5},
    1:{'nome':'Claymore','tipo':'Arma','danno':10},
    2:{'nome':'Ammazzadraghi','tipo':'Arma','danno':15}
}

def assign_weapon(player, weapon_id):
    weapon_info = weapon_item_tier_1[weapon_id]
    player.weapon = Weapon(weapon_info['nome'],['arma'],['danno'])
#???????????????????????????????????????????????????????????????????????




