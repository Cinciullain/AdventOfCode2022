from enum import Enum


class Valori(Enum):
    X = 1  # Rock     A
    Y = 2  # Paper    B
    Z = 3  # Scissors C
    LOSS = 0
    DRAW = 3
    WIN = 6


# Salvo il contenuto del file in una lista
with open("Day2/input.txt", "r") as file:
    righeFile = file.readlines()

# Rimuovo il carattere \n e lo spazio
for i in range(len(righeFile)):
    righeFile[i] = righeFile[i][:-1].replace(' ', '')

print(righeFile)
