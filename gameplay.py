import random
from scelta_utente import get_user_choice
#from functions import start_menu

def start_game(enemy,giocatore):
    print("Attenzione!",enemy.name,"ti sta attaccando! possiede",enemy.hp,"punti ferita, e tanta voglia di menare, preparati!!!")
    
    while enemy.hp > 0 and giocatore.hp > 0:
        print("cosa vuoi fare? 1=attacco, 2=un cazzo perchè non puoi fare altro")
        azione = get_user_choice(">",2)
        
        if azione != 1 and azione != 2:
            print("""  
            *******************************************************
            Ma sei cojone? non me pare d'avette dato st'opzione
                                RICOMINCIA 
            *******************************************************
            """)
            break  
        exit
        
        if azione == 1:
            from functions import start_menu, level_up
            playerturn = random.randint(1,20)
            enemyturn = random.randint(1,20)
            
            if playerturn == enemyturn:
                print("LE VOSTRE ARMI SI SCONTRANO ALLA PARI! NON SUCCEDE UN CAZZO VAI ATTACCA ATTACCAA")
                
            if playerturn > enemyturn:
                enemy.hp -= giocatore.atk
                print("\n",giocatore.name,"hai fatto",giocatore.atk,"danni! Il mostro è rimasto con",enemy.hp,"punti ferita!")

                if enemy.hp <= 0:
                    print("IL TUO AVVERSARIO E' STATO SCONFITTO! DAJE ZI")
                    print("Hai guadagnato",enemy.exp,"punti esperienza!")
                    giocatore.exp += enemy.exp
                
                    if giocatore.exp >= giocatore.exp_pool:
                        level_up(giocatore)
                        print("Ora sei al livello",giocatore.lv,"!!!")
                        input(">")
                        start_menu(giocatore)
                    else:
                        start_menu(giocatore)
                        
                else:
                    attacco_nemico = random.randint(enemy.minatk,enemy.maxatk)
                    giocatore.hp -= attacco_nemico
                    print("il mostro ti colpisce per",attacco_nemico,"danni!",giocatore.name,",ti restano",giocatore.hp,"punti ferita!\n")
                    if giocatore.hp <= 0:
                        print("BER COJONE SEI MORTO")
                        input(">")
                        
                        start_menu(giocatore)
                
            if enemyturn > playerturn:
                attacco_nemico = random.randint(enemy.minatk,enemy.maxatk)
                giocatore.hp -= attacco_nemico
                print("\nil mostro ti colpisce per",attacco_nemico,"danni!",giocatore.name,",ti restano",giocatore.hp,"punti ferita!")
                
                if giocatore.hp <= 0:
                    print("BER COJONE SEI MORTO")
                    input(">")
                    
                    start_menu(giocatore)
                
                else:
                    enemy.hp -= giocatore.atk
                    print("\n",giocatore.name,"hai fatto",giocatore.atk,"danni! Il mostro è rimasto con",enemy.hp,"punti ferita!\n")
                    if enemy.hp <= 0:
                        print("IL TUO AVVERSARIO E' STATO SCONFITTO! DAJE ZI")
                        print("Hai guadagnato",enemy.exp,"punti esperienza!")
                        giocatore.exp += enemy.exp
                        if giocatore.exp >= giocatore.exp_pool:
                            level_up(giocatore)
                            print("Ora sei al livello",giocatore.lv,"!!!")
                            input(">")
                            start_menu(giocatore)
                        else:
                            start_menu(giocatore)
    return giocatore                      

#raccoglie i valori dal def e printa l'indice del valore interessato
#print(f"Il tuo avversario è un/una", select_challenge(0),"con",select_challenge(1),"punti ferita, preparati!!!")
#print("cosa vuoi fare? 1=attacco, ,3=un cazzo perchè non puoi fare altro")


#