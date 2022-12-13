# Inizio programma
# Salvo il contenuto del file in una lista
with open("Day7/input.txt", "r") as file:
    righeFile = file.readlines()

# Rimuovo il carattere \n
for i in range(len(righeFile)):
    righeFile[i] = righeFile[i][:-1]


c = "7"
print(c)

c += "8"
print(c)