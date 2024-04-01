import random as r

lista_elementi = [
    {'sigla': 'Li', 'number': 3, 'nome': 'Litio', 'categoria': 'Metallo', 'stato': "solido"},
    {'sigla': 'Na', 'number': 11, 'nome': 'Sodio', 'categoria': 'Metallo', 'stato': "solido"},
    {'sigla': 'Mg', 'number': 12, 'nome': 'Magnesio', 'categoria': 'Metallo', 'stato': "solido"},
    {'sigla': 'Al', 'number': 13, 'nome': 'Alluminio', 'categoria': 'Metallo', 'stato': "solido"},
    {'sigla': 'K', 'number': 19, 'nome': 'Potassio', 'categoria': 'Metallo', 'stato': "solido"},
    {'sigla': 'Ca', 'number': 20, 'nome': 'Calcio', 'categoria': 'Metallo', 'stato': "solido"},
    {'sigla': 'Ti', 'number': 22, 'nome': 'Titanio', 'categoria': 'Metallo', 'stato': "solido"},
    {'sigla': 'V', 'number': 23, 'nome': 'Vanadio', 'categoria': 'Metallo', 'stato': "solido"},
    {'sigla': 'Cr', 'number': 24, 'nome': 'Cromo', 'categoria': 'Metallo', 'stato': "solido"},
    {'sigla': 'Mn', 'number': 25, 'nome': 'Manganese', 'categoria': 'Metallo', 'stato': "solido"},
    {'sigla': 'Fe', 'number': 26, 'nome': 'Ferro', 'categoria': 'Metallo', 'stato': "solido"},
    {'sigla': 'Co', 'number': 27, 'nome': 'Cobalto', 'categoria': 'Metallo', 'stato': "solido"},
    {'sigla': 'Ni', 'number': 28, 'nome': 'Nichel', 'categoria': 'Metallo', 'stato': "solido"},
    {'sigla': 'Cu', 'number': 29, 'nome': 'Rame', 'categoria': 'Metallo', 'stato': "solido"},
    {'sigla': 'Ga', 'number': 31, 'nome': 'Gallio', 'categoria': 'Metallo', 'stato': "solido"},
    {'sigla': 'Ge', 'number': 32, 'nome': 'Germanio', 'categoria': 'Metallo', 'stato': "solido"},
    {'sigla': 'Ag', 'number': 47, 'nome': 'Argento', 'categoria': 'Metallo', 'stato': "solido"},
    {'sigla': 'Sn', 'number': 50, 'nome': 'Stagno', 'categoria': 'Metallo', 'stato': "solido"},
    {'sigla': 'W', 'number': 74, 'nome': 'Wolfranio/Tungsteno', 'categoria': 'Metallo', 'stato': "solido"},
    {'sigla': 'Pt', 'number': 78, 'nome': 'Platino', 'categoria': 'Metallo', 'stato': "solido"},
    {'sigla': 'Au', 'number': 79, 'nome': 'Oro', 'categoria': 'Metallo', 'stato': "solido"},
    {'sigla': 'Hg', 'number': 80, 'nome': 'Mercurio', 'categoria': 'Metallo', 'stato': "Licquido"},
    {'sigla': 'Pb', 'number': 82, 'nome': 'Piombo', 'categoria': 'Metallo', 'stato': "solido"},
    {'sigla': 'Si', 'number': 14, 'nome': 'Silicio', 'categoria': 'Semi-metalli', 'stato': "solido"},
    {'sigla': 'As', 'number': 33, 'nome': 'Arsenico', 'categoria': 'Semi-metalli', 'stato': "solido"},
    {'sigla': 'H', 'number': 1, 'nome': 'Idrogeno', 'categoria': 'Non-metalli', 'stato': "gas"},
    {'sigla': 'N', 'number': 7, 'nome': 'Azoto', 'categoria': 'Non-metalli', 'stato': "gas"},
    {'sigla': 'O', 'number': 8, 'nome': 'Ossigeno', 'categoria': 'Non-metalli', 'stato': "gas"},
    {'sigla': 'F', 'number': 9, 'nome': 'Fluoro', 'categoria': 'Non-metalli', 'stato': "gas"},
    {'sigla': 'Cl', 'number': 17, 'nome': 'Cloro', 'categoria': 'Non-metalli', 'stato': "gas"},
    {'sigla': 'Br', 'number': 35, 'nome': 'Bromo', 'categoria': 'Non-metalli', 'stato': "licquido"},
    {'sigla': 'C', 'number': 6, 'nome': 'Carbonio', 'categoria': 'Non-metalli', 'stato': "solido"},
    {'sigla': 'P', 'number': 15, 'nome': 'Fosforo', 'categoria': 'Non-metalli', 'stato': "solido"},
    {'sigla': 'S', 'number': 16, 'nome': 'Zolfo', 'categoria': 'Non-metalli', 'stato': "solido"},
    {'sigla': 'Se', 'number': 34, 'nome': 'Selenio', 'categoria': 'Non-metalli', 'stato': "solido"},
    {'sigla': 'I', 'number': 53, 'nome': 'Iodio', 'categoria': 'Non-metalli', 'stato': "solido"},
    {'sigla': 'He', 'number': 2, 'nome': 'Helio', 'categoria': 'Gas-nobili', 'stato': "gas"},
    {'sigla': 'Ne', 'number': 10, 'nome': 'Neon', 'categoria': 'Gas-nobili', 'stato': "gas"},
    {'sigla': 'Ar', 'number': 18, 'nome': 'Argo', 'categoria': 'Gas-nobili', 'stato': "gas"},
    {'sigla': 'Kr', 'number': 36, 'nome': 'Kripto', 'categoria': 'Gas-nobili', 'stato': "gas"},
    {'sigla': 'Xe', 'number': 54, 'nome': 'Xenio', 'categoria': 'Gas-nobili', 'stato': "gas"},
    {'sigla': 'Rn', 'number': 86, 'nome': 'Radon', 'categoria': 'Gas-nobili', 'stato': "gas"}
]

def risposta_Corretta():
    print("\033[32m")
    print("risposta Corretta")
    print("\033[37m")

def risposta_Errata(elemento_randomico, categoria):
    print("\033[31m")
    print(f"risposta errata, la corretta => {lista_elementi[elemento_randomico][categoria]}")
    print("\033[37m")


def Game():
    print("benvenuto nel mio gioco")

    print('''
Informazioni:
    -Ti fornisco la sigla atomica tu devi indovinare il resto\n
Metodo di gioco:
    -Inserisci il numero
    -Inserisci il nome dell'elemento
    -Inserisci lo stato della materia
''')
    if input("sei pronto y/n\n") == "y":
        print("------------inizzializzazione-----------------")
        while True:
            elemento_randomico = r.randint(0, len(lista_elementi)-1)
            lista_numeri = []
            for number in lista_numeri:
                if elemento_randomico in lista_numeri:
                    elemento_randomico = r.randint(0, len(lista_elementi)-1)
                else:pass

            print(lista_elementi[elemento_randomico]["sigla"])

            print("ora forniscimi il suo nome :")
            if input() == lista_elementi[elemento_randomico]["nome"]:
                risposta_Corretta()
            else:
                risposta_Errata(elemento_randomico=elemento_randomico, categoria="nome")

            print("forniscimi il numero atomico :")
            if int(input()) == lista_elementi[elemento_randomico]["number"]:
                risposta_Corretta()
            else:
                risposta_Errata(elemento_randomico=elemento_randomico, categoria="number")

            print("(possibilità => Metallo/Semi-metalli/Non-metalli/Gas-nobili)\nora forniscimi la sua categoria:")
            if input() == lista_elementi[elemento_randomico]["categoria"]:
                risposta_Corretta()
            else:
                risposta_Errata(elemento_randomico=elemento_randomico, categoria="categoria")  

            print("(possibilità => solido/licquido/gas)\nora forniscimi il suo stato:")
            if input() == lista_elementi[elemento_randomico]["stato"]:
                risposta_Corretta()
            else:
                risposta_Errata(elemento_randomico=elemento_randomico, categoria="stato")  

            lista_numeri.append(elemento_randomico)
            print("-----------------divisorio---------------------")
    else:
        print("perché lo hai avviato :(")
        pass

if __name__=="__main__":
    Game()