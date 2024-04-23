from TXTRPG import giocatore,exp_pool,select_challenge

def start_menu(load_save, player_stats, settings, heal):
    
    print("""
    Quindi,""",giocatore.name,""",Ora che siamo pronti, scegli cosa fare!
    Premi:

    1) Gioca!
    2) Carica salvataggio(work in progress)
    3) Statistiche giocatore
    4) Impostazioni
    5) Esci
    6) Heal
    """)
    choice = int(input(">"))
    
    if choice == 1:
        if giocatore.hp <= 0:
            print("DOVE CAZZO VAI CO",giocatore.hp,"DI VITA?? CURATI")
            start_menu()
        else:
            enemy = select_challenge()

    elif choice == 2: 
        load_save()

    elif choice == 3:
        player_stats(exp_pool)

    elif choice == 4:
        nome = settings()
        giocatore.name = nome
        
    elif choice == 5:
        print("Sei sicuro di voler uscire? ti caghi? 1 Per uscire 0 per tornare al menu")
        close = int(input(">"))
        if close == 1:
            print("a merda")
            input("")
            exit()
        elif close == 0:
            print("v-Prego di qua, mi segua-v")
            start_menu()
    
    elif choice == 6:
        heal()

    else:
        print("immissione non valida, daje mpò")
        start_menu()   