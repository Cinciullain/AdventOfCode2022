# Inizio programma
# Salvo il contenuto del file in una lista
with open("Day5/input.txt", "r") as file:
    righeFile = file.readlines()

# Rimuovo il carattere \n e lo spazio
for i in range(len(righeFile)):
    righeFile[i] = righeFile[i][:-1]

# Creo uno stack per ogni colonna
stack0 = []
stack1 = []
stack2 = []
stack3 = []
stack4 = []
stack5 = []
stack6 = []
stack7 = []
stack8 = []

contatoreStack = 0
for i in range(8):
    # Ho deciso di farlo hardcode finchè non trovo un modo migliore
    stack0.append(righeFile[i][1])

    if righeFile[i][5] != ' ':
        stack1.append(righeFile[i][5])

    if righeFile[i][9] != ' ':
        stack2.append(righeFile[i][9])

    if righeFile[i][13] != ' ':
        stack3.append(righeFile[i][13])

    if righeFile[i][17] != ' ':
        stack4.append(righeFile[i][17])

    if righeFile[i][21] != ' ':
        stack5.append(righeFile[i][21])

    if righeFile[i][25] != ' ':
        stack6.append(righeFile[i][25])

    if righeFile[i][29] != ' ':
        stack7.append(righeFile[i][29])

    if righeFile[i][33] != ' ':
        stack8.append(righeFile[i][33])

# Creo una lista di stack
stackList = [stack0, stack1, stack2, stack3, stack4, stack5, stack6, stack7, stack8]
# Finita la parte di riempimento degli stack, inizio a controllare i valori del resto del file

for i in range(10, len(righeFile)):
    righeFile[i] = righeFile[i].replace("move ", "").replace("from ", "").replace("to ", "") + " "
    quanti = 0
    daDove = 0
    perDove = 0
    contatore = 0
    numero = ""
    for j in range(len(righeFile[i])):
        if righeFile[i][j] == " ":
            if contatore == 0:
                quanti = int(numero)
                numero = ""
            elif contatore == 1:
                daDove = int(numero)
                numero = ""
            elif contatore == 2:
                perDove = int(numero)
                numero = ""
            contatore += 1
        else:
            numero += righeFile[i][j]

    # Inizio a spostare i dischi
    # Arrivato qua ho i numeri
    # Ho finito di leggere la riga, ora devo spostare i dischi
    while quanti > 0:
        stackList[perDove - 1].append(stackList[daDove - 1].pop())
        quanti -= 1

# Ora prendo la cima di ogni stack
cime = ""
for i in range(len(stackList)):
    cime += stackList[i].pop()

print(cime)
