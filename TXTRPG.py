from functions import giocatore,header,start_menu,select_challenge,load_save,player_stats,settings,heal

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

header()

print("E allora ti porgo il mio benvenuto""",giocatore.name,""",per ora, attaccherai solo, non ci sono altre opzioni, un mostro verrà scelto in base alla difficoltà e durante il combattimento,
    l'ordine d'attacco sarà casuale: quindi sostanzialmente continua ad attaccare e spera di vincere!""")
start_menu(select_challenge,load_save,player_stats,settings,heal)



