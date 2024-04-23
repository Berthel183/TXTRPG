import random


def start_game(enemy,giocatore,exp_pool):

    print("Attenzione!",enemy.name,"ti sta attaccando! possiede",enemy.hp,"punti ferita, e tanta voglia di menare, preparati!!!")
    
    while enemy.hp > 0 and giocatore.hp > 0:
        print("cosa vuoi fare? 1=attacco, 2=un cazzo perchè non puoi fare altro")
        azione = int(input(">"))
        
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
                    giocatore.exp + enemy.exp
                    if giocatore.exp == exp_pool:
                        print("Ora sei al livello",giocatore.lv+1,"!!!")
                        input(">")
                        from menu import start_menu
                        start_menu()
                        
                else:
                    attacco_nemico = random.randint(enemy.minatk,enemy.maxatk)
                    giocatore.hp -= attacco_nemico
                    print("il mostro ti colpisce per",attacco_nemico,"danni!",giocatore.name,",ti restano",giocatore.hp,"punti ferita!\n")
                    if giocatore.hp <= 0:
                        print("BER COJONE SEI MORTO")
                        input(">")
                        from menu import start_menu
                        start_menu()
                
            if enemyturn > playerturn:
                attacco_nemico = random.randint(enemy.minatk,enemy.maxatk)
                giocatore.hp -= attacco_nemico
                print("\nil mostro ti colpisce per",attacco_nemico,"danni!",giocatore.name,",ti restano",giocatore.hp,"punti ferita!")
                
                if giocatore.hp <= 0:
                    print("BER COJONE SEI MORTO")
                    input(">")
                    from menu import start_menu
                    start_menu()
                
                else:
                    enemy.hp -= giocatore.atk
                    print("\n",giocatore.name,"hai fatto",giocatore.atk,"danni! Il mostro è rimasto con",enemy.hp,"punti ferita!\n")
                    if enemy.hp <= 0:
                        print("IL TUO AVVERSARIO E' STATO SCONFITTO! DAJE ZI")
                        print("Hai guadagnato",enemy.exp,"punti esperienza!")
                        giocatore.exp + enemy.exp
                        if giocatore.exp == exp_pool:
                            print("Ora sei al livello",giocatore.lv+1,"!!!")
                            input(">")
                            from menu import start_menu
                            start_menu()
    return giocatore                      

#raccoglie i valori dal def e printa l'indice del valore interessato
#print(f"Il tuo avversario è un/una", select_challenge(0),"con",select_challenge(1),"punti ferita, preparati!!!")
#print("cosa vuoi fare? 1=attacco, ,3=un cazzo perchè non puoi fare altro")


#