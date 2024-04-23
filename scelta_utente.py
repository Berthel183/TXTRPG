def get_user_choice(prompt, num_options):
    while True:
        try:
            choice = int(input(prompt))
            if 1 <= choice <= num_options:
                return choice
            else:
                print("non è un'opzione valida! premi un tasto qualsiasi e inserisci un numero tra 1 e {num_options}.")
        except ValueError:
            print("Inserisci un numero valido!")