# Inizio programma
# Salvo il contenuto del file in una lista
with open("Day7/input.txt", "r") as file:
    righeFile = file.readlines()

# Rimuovo il carattere \n
for i in range(len(righeFile)):
    righeFile[i] = righeFile[i][:-1]


# Devo trovare il numero di cartelle la cui somma totale della dimensione sia >= 100000
# Devo trovare un modo per salvare tutti i dati e potervi accedere in modo efficente, come una hashmap o un dizionario

dirCorrente = []
dirNuova = ""
listaBase = []
for riga in righeFile:
    riga = riga.split(" ")
    if riga[0] == "$":
        if riga[1] == "cd":
            # siamo in cd

            if riga[2] == "..":
                print("cartella prima")
                dirCorrente.pop()
            else:
                print("cartella indicata")
                dirCorrente.append(riga[2])

        else:
            continue
            # print("siamo in ls")

    elif riga[0] == "dir":
        print("crea cartella")
        listaSupporto = [riga[1]]
        listaBase.append(listaSupporto)

    else:
        print("crea file")
