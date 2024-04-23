import random
from scelta_utente import get_user_choice

class Enemy:
    def __init__(self,name,hp,minatk,maxatk,exp):
        self.name = name
        self.hp = hp
        self.minatk = minatk
        self.maxatk = maxatk
        self.exp = exp

class Player:
    def __init__(self,name,hp,atk,exp,lv,maxhp):
        self.name = name
        self.hp = hp
        self.atk = atk  
        self.exp = exp
        self.lv = lv      
        self.maxhp = maxhp


giocatore = Player(0,50,12,0,1,50)
enemy = Enemy(0,0,0,0,0)
exp_pool = 10
lvcount = 0

#ctrl k c / ctrl k u

print("""
    -------------------------------------------------------
    |######### #      #  #########  ######  ######  ######|
    |    #      #   #        #      #    #  #    #  #     |
    |    #        #          #      #  #    # ####  #   ##|
    |    #       # #         #      #   #   #       #    #|
    |    #     #     #       #      #    #  #       ######|
    -------------------------------------------------------
      """)
print("""
      COME FUNZIONA: Per ora, attaccherai solo, non ci sono altre opzioni, un mostro verrà scelto in base alla  
      difficoltà e durante il combattimento, l'ordine d'attacco sarà casuale: quindi sostanzialmente continua ad  
      attaccare (tasto 1) e spera di vincere!
      """)


def header():
        print("Ti stai approcciando al magico mondo di TXTRPG, ma ho bisogno di sapere il tuo nome!")
        nome_iniziale = str(input(">"))
        print("Ti vuoi chiamare,",nome_iniziale,"? 1 per confermare, 2 per inserire un altro nome")
        choice = get_user_choice("",2)

        if choice == 2:
            print("Hai confermato il tuo nome!")
            header("allora, ricominciamo!")
        elif choice == 1:        
            print("Hai confermato il tuo nome!")
    
        giocatore.name = nome_iniziale
        return giocatore
header()


def player_stats(exp_pool):
    
    if giocatore.exp < exp_pool:
        print("Ciao",giocatore.name,", ecco le tue statistiche!")
        print("Vita massima:",giocatore.maxhp)
        print("Vita:",giocatore.hp)
        print("Attacco:",giocatore.atk)
        print("livello:",giocatore.lv)
        print("Esperienza:",giocatore.exp,"\n")
        from menu import start_menu
        
    #for player_exp in exp_pool:
    else:
        print(exp_pool,"EXP POOL PRINT PRIMA")
        exp_pool += 10
        print(exp_pool,"EXP POOL PRINT")
        giocatore.maxhp += 10
        giocatore.atk += 4
        print(giocatore.exp,"GIOCATORE EXP PRINT PRIMA")
        giocatore.exp = 0
        print(giocatore.exp,"GIOCATORE EXP PRINT")
        giocatore.lv += lvcount
        giocatore.hp = giocatore.maxhp
        print("Vita:",giocatore.hp)
        print("Attacco:",giocatore.atk)
        print("Esperienza",giocatore.exp,"\n")
        from menu import start_menu
        

print("E allora ti porgo il mio benvenuto""",giocatore.name,""",per ora, attaccherai solo, non ci sono altre opzioni, un mostro verrà scelto in base alla difficoltà e durante il combattimento,
    l'ordine d'attacco sarà casuale: quindi sostanzialmente continua ad attaccare e spera di vincere!""")

from menu import start_menu
start_menu()

def settings():

    print("""Cosa vuoi fare?
          1) Cambia nome giocatore
          2) esci
          """)    

    choice = choice = get_user_choice()
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
        from menu import start_menu

    else:
        print("immissione non valida, me stai a perculà? dai fa il serio va a sceglie")
        settings() 

def load_save():

    print("Da qui potrai caricare un file con i tuoi progressi! come si chiama il file? sii molto preciso, con tanto di estensione!")
    print("compra il dlc per salvare i progressi, per ora torna al menù")
    input("Premi qualsiasi tasto per proseguire")
    from menu import start_menu
    importsave = input(">")

def heal():
    print("Un cerusico ti trova e ti riattoppa le ferite!")
    giocatore.hp = giocatore.maxhp    
    print("Hai",giocatore.hp,"punti ferita ora!")
    input("press any")
    from menu import start_menu

def select_challenge():
    
    print("Allora",giocatore.name,"che mostro vuoi affrontare? Scegli una difficoltà tra 1, 2 o 3, 4 se popo t'aregge, invio per confermare o CTRL+C per uscire")
    enemylist1 = ("Topo","Pesce","Sedia","Tizio")
    enemylist2 = ("Scheletro","Mannaro","Gorillone","Mago")
    enemylist3 = ("Drago","Lich","Golem","Flayer")
    enemylist4 = ("GOD")
    
    challenge = int(input(">"))
    
    if challenge == 1:
        enemy.name = random.choice(enemylist1)
        enemy.hp = random.randint(50,80)
        enemy.minatk = 5
        enemy.maxatk = 10
        enemy.exp = 5
        #drop_item_weapon
        #drop_item_armor

    elif challenge == 2:
        enemy.name = random.choice(enemylist2)
        enemy.hp = random.randint(80,120)
        enemy.minatk = 15
        enemy.maxatk = 20
        enemy.exp = 10
       
    elif challenge == 3:
        enemy.name = random.choice(enemylist3)
        enemy.hp = random.randint(130,170)
        enemy.minatk = 20
        enemy.maxatk = 30
        enemy.exp = 20

    elif challenge == 4:
        enemy.name = (enemylist4)
        enemy.hp = random.randint(9999,9999)
        enemy.minatk = 666
        enemy.maxatk = 1337
        enemy.exp = 500
        
    else:
        print("immissione non valida, te risparo il pippone, premi qualcosa")
        input(">cojone<")
        select_challenge()

    return enemy
 



