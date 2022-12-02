#Codice un pò bruttino, ma funziona, da rifare con un approccio più corretto e non hardcoded

#from enum import Enum

#class Valori(Enum):
X = 1  # Rock     A
Y = 2  # Paper    B
Z = 3  # Scissors C
LOSS = 0
DRAW = 3
WIN = 6

#PARTE 1
#AX = X + DRAW
#AY = Y + WIN
#AZ = Z + LOSS
#BX = X + LOSS
#BY = Y + DRAW
#BZ = Z + WIN
#CX = X + WIN
#CY = Y + LOSS
#CZ = Z + DRAW

#PARTE 2
AX = LOSS + Z
AY = X + DRAW
AZ = Y + WIN
BX = X + LOSS
BY = DRAW + Y
BZ = WIN + Z
CX = LOSS + Y
CY = DRAW + Z
CZ = X + WIN


# Salvo il contenuto del file in una lista
with open("Day2/input.txt", "r") as file:
    righeFile = file.readlines()

# Rimuovo il carattere di ritorno a capo
for i in range(len(righeFile)):
    righeFile[i] = righeFile[i][:-1]

punteggioGiocatore = 0
games = []
for i in range(len(righeFile)):
    game = ""
    game += righeFile[i][0]
    game += righeFile[i][2]
    games.append(game)

for i in games:
    if i == "AX":
        punteggioGiocatore += AX
    elif i == "AY":
        punteggioGiocatore += AY
    elif i == "AZ":
        punteggioGiocatore += AZ
    elif i == "BX":
        punteggioGiocatore += BX
    elif i == "BY":
        punteggioGiocatore += BY
    elif i == "BZ":
        punteggioGiocatore += BZ
    elif i == "CX":
        punteggioGiocatore += CX
    elif i == "CY":
        punteggioGiocatore += CY
    elif i == "CZ":
        punteggioGiocatore += CZ


print(punteggioGiocatore)
