#Funzioni contenute:header, player_stats, settings, load_save, heal, select_challenge, 
from scelta_utente import get_user_choice
from gameplay import start_game
import random

class Player:
    def __init__(self,name,hp,atk,exp,lv,maxhp,exp_pool,equip):
        self.name = name
        self.hp = hp
        self.atk = atk  
        self.exp = exp
        self.lv = lv      
        self.maxhp = maxhp
        self.exp_pool = exp_pool
        self.equip: list[Equip] = []

class Enemy:
    def __init__(self,name,hp,minatk,maxatk,exp):
        self.name = name
        self.hp = hp
        self.minatk = minatk
        self.maxatk = maxatk
        self.exp = exp

class Equip:
    def __init__(self,equip_name,equip_type):
        self.equip_name = equip_name
        self.equip_type = equip_type

class Weapon(Equip):
    def __init__ (self,equip_name,equip_type,atk_bonus): #sempre riportare le proprietà del genitore
        super().__init__(equip_name,equip_type)
        self.atk_bonus: int = atk_bonus #specificato int, non necessario
        

class Helm(Equip):
    pass

class Shield(Equip):
    pass

class Chest(Equip):
    pass


class Bonus_Equip:
    def __init__(self,atk_bonus,def_bonus,hp_bonus):
        
        self.def_bonus = def_bonus
        self.hp_bonus = hp_bonus


giocatore = Player(0,50,12,0,1,50,10,0)
enemy = Enemy(0,0,0,0,0)
equip = Bonus_Equip(0,0,0)
arma = Weapon('','',0)  #istanziamento della classe


def total_atk(giocatore):
    giocatore.atk += giocatore.equip



#Intro e primo input per creazione nome
def header():
    print("Ti stai approcciando al magico mondo di TXTRPG, ma ho bisogno di sapere il tuo nome!")
    nome_iniziale = str(input(">"))
    print("Ti vuoi chiamare,",nome_iniziale,"? 1 per confermare, 2 per inserire un altro nome")
    choice = get_user_choice("",2)

    if choice == 1:        
        print("Hai confermato il tuo nome!")
        giocatore.name = nome_iniziale
        return giocatore
    elif choice == 2:
        print("allora, ricominciamo!")
        header()
    start_menu(giocatore)
    
#Menù principale di gioco
def start_menu(giocatore):
    
    print("""
    Quindi,""",giocatore.name,""",Ora che siamo pronti, scegli cosa fare!
    Premi:

    1) Gioca!
    2) Carica salvataggio(work in progress)
    3) Statistiche giocatore
    4) Impostazioni
    5) Heal
    6) Esci
    
    """)
    choice = get_user_choice(">",6)
    
    if choice == 1:
        if giocatore.hp <= 0:
            print("DOVE CAZZO VAI CO",giocatore.hp,"DI VITA?? CURATI",input("/>Premi un tasto!"))
            start_menu(giocatore)
        else:
            select_challenge()
            start_game(enemy,giocatore)
    elif choice == 2: 
        load_save()

    elif choice == 3:
        player_stats(giocatore)

    elif choice == 4:
        nome = settings()
        giocatore.name = nome
    
    elif choice == 5:
        heal(giocatore)

    elif choice == 6:
        print("Sei sicuro di voler uscire? ti caghi? 1 Per uscire 0 per tornare al menu")
        close = int(input(">"))
        if close == 1:
            print("a merda")
            input("")
            exit()
        elif close == 0:
            print("v-Prego di qua, mi segua-v")
            start_menu(giocatore)

    else:
        print("immissione non valida, daje mpò")
        start_menu(giocatore)   

#def main_menu(giocatore):
    

#STATISTICHE PLAYER
def player_stats(giocatore):
    
    print("Ciao",giocatore.name,", ecco le tue statistiche!")
    print("Vita massima:",giocatore.maxhp)
    print("Vita:",giocatore.hp)
    print("Attacco:",giocatore.atk)
    print("livello:",giocatore.lv)
    print("Esperienza:",giocatore.exp,"\n")

    input('premi qualsiasi tasto per tornare al menù!')
    start_menu(giocatore)

def level_up(giocatore):       
    #for giocatore.exp in giocatore.exp_pool:
    while giocatore.exp >= giocatore.exp_pool:
        #print(giocatore.exp_pool,"EXP POOL PRINT PRIMA")
        
        giocatore.exp -= giocatore.exp_pool #toglie dalla exp del giocatore il valore di pool raggiunto
        giocatore.exp_pool += 10   #incrementa il pool da raggiungere di 10
        print("Devi raggiungere ",giocatore.exp_pool," PE per il prossimo livello!")
        giocatore.maxhp += 10
        giocatore.atk += 4
        #print("Attualmente hai ",giocatore.exp," PE")
        giocatore.lv += 1
        giocatore.hp = giocatore.maxhp

        print("Vita:",giocatore.hp)
        print("Attacco:",giocatore.atk)
        print("Esperienza",giocatore.exp,"\n")

    input('premi qualsiasi tasto per tornare al menù!')
    start_menu(giocatore)

#IMPOSTAZIONI
def settings():  

    choice = get_user_choice(
        """Cosa vuoi fare?
        1) Cambia nome giocatore
        2) esci
        """,2)
    if choice == 1:

        print("Come vuoi essere chiamato? Scegli un nome, non giudichiamo")
        nome_giocatore = str(input(""))
        print("BRAVISSIMO!! ORA TI CHIAMI ||*",nome_giocatore,"*|| !!\n")
        input("Premi un tasto qualsiasi per continuare")
        giocatore.name = nome_giocatore
        settings()
        return

    elif choice == 2:
        print("v-Prego di qua, mi segua-v")
        start_menu(giocatore)

    else:
        print("immissione non valida, me stai a perculà? dai fa il serio va a sceglie")
        settings() 

#CARICA SALVATAGGIO - WORK IN PROGRESS -
def load_save():

    print("Da qui potrai caricare un file con i tuoi progressi! come si chiama il file? sii molto preciso, con tanto di estensione!")
    print("compra il dlc per salvare i progressi, pe ora premi qualsiasi tasto per proseguire")
    input(">")
    importsave = input(">")
    start_menu(giocatore)

#CURA, SET HP TO MAX
def heal(giocatore):
    print("Un cerusico ti trova e ti riattoppa le ferite!")
    giocatore.hp = giocatore.maxhp    
    print("Hai",giocatore.hp,"punti ferita ora!")
    input('premi qualsiasi tasto per tornare al menù!')
    start_menu(giocatore)

#SELEZIONE DIFFICOLTA' E SCELTA NEMICO
def select_challenge():
    print("Allora",giocatore.name,"che mostro vuoi affrontare? Scegli una difficoltà tra 1, 2 o 3, 4 se popo t'aregge, invio per confermare o CTRL+C per uscire")
    enemylist1 = ("Topo","Pesce","Sedia","Tizio")
    enemylist2 = ("Scheletro","Mannaro","Gorillone","Mago")
    enemylist3 = ("Drago","Lich","Golem","Flayer")
    enemylist4 = ("GOD")
    
    challenge = get_user_choice(">",4)
    
    if challenge == 1:
        enemy.name = random.choice(enemylist1)
        enemy.hp = random.randint(50,80)
        enemy.minatk = 5
        enemy.maxatk = 10
        enemy.exp = 5
        # #drop_item_weapon
        # #drop_item_armor
        return enemy

    elif challenge == 2:
        enemy.name = random.choice(enemylist2)
        enemy.hp = random.randint(80,120)
        enemy.minatk = 15
        enemy.maxatk = 20
        enemy.exp = 10
        return enemy

    elif challenge == 3:
        enemy.name = random.choice(enemylist3)
        enemy.hp = random.randint(130,170)
        enemy.minatk = 20
        enemy.maxatk = 30
        enemy.exp = 20
        return enemy

    elif challenge == 4:
        enemy.name = (enemylist4)
        enemy.hp = random.randint(9999,9999)
        enemy.minatk = 666
        enemy.maxatk = 1337
        enemy.exp = 500
        return enemy

    else:
        print("immissione non valida, te risparo il pippone, premi qualcosa")
        input(">cojone<")
        select_challenge()
    
    

#start_menu(select_challenge,load_save,player_stats,settings,heal)



