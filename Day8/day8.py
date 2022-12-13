# Inizio programma
# Salvo il contenuto del file in una lista
with open("Day8/input.txt", "r") as file:
    righeFile = file.readlines()

# Rimuovo il carattere \n e lo spazio
for i in range(len(righeFile)):
    righeFile[i] = righeFile[i][:-1]

print(righeFile)