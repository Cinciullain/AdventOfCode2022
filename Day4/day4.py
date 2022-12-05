# Inizio programma
# Salvo il contenuto del file in una lista
with open("Day4/input.txt", "r") as file:
    righeFile = file.readlines()

# Rimuovo il carattere \n e lo spazio
for i in range(len(righeFile)):
    righeFile[i] = righeFile[i][:-1]

# Inizio parte 1
inizioPrimo = ""
finePrimo = ""
inizioSecondo = ""
fineSecondo = ""
sovrapposizioni = 0
sovrapposizioni2 = 0

for i in range(len(righeFile)):
    inizioPrimo = righeFile[i].split('-')[0]
    finePrimo = righeFile[i].split('-')[1].split(',')[0]
    inizioSecondo = righeFile[i].split('-')[1].split(',')[1]
    fineSecondo = righeFile[i].split('-')[2]

    if int(inizioPrimo) <= int(fineSecondo) <= int(finePrimo):
        sovrapposizioni2 += 1
    elif int(inizioSecondo) <= int(finePrimo) <= int(fineSecondo):
        sovrapposizioni2 += 1
    elif int(inizioPrimo) <= int(inizioSecondo) <= int(finePrimo):
        sovrapposizioni2 += 1
    elif int(inizioSecondo) <= int(inizioPrimo) <= int(fineSecondo):
        sovrapposizioni2 += 1

    if int(inizioPrimo) <= int(inizioSecondo) <= int(fineSecondo) <= int(finePrimo):
        sovrapposizioni += 1
    elif int(inizioSecondo) <= int(inizioPrimo) <= int(finePrimo) <= int(fineSecondo):
        sovrapposizioni += 1

print(sovrapposizioni, sovrapposizioni2)