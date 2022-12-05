# A parte da 65 in ASCII, quindi siccome bisogna avere 27 come valore, si fa 65 - 38 = 27
# a parte da 97 in ASCII, quindi siccome bisogna avere 1 come valore, si fa 97 - 96 = 1

# Inizio programma
# Salvo il contenuto del file in una lista
with open("Day3/input.txt", "r") as file:
    righeFile = file.readlines()

# Rimuovo il carattere \n e lo spazio
for i in range(len(righeFile)):
    righeFile[i] = righeFile[i][:-1]

charAttuale = ''
primaMeta = ""
secondaMeta = ""
lunghezzaInv = 0
sommaTot = 0
for inv in righeFile:
    lunghezzaInv = len(inv)
    primaMeta = inv[:lunghezzaInv // 2]
    secondaMeta = inv[lunghezzaInv // 2:]

    for i in range(lunghezzaInv // 2):
        charAttuale = primaMeta[i]
        if secondaMeta.__contains__(charAttuale):
            if charAttuale.isupper():
                sommaTot += ord(charAttuale) - 38
                break
            else:
                sommaTot += ord(charAttuale) - 96
                break

print(sommaTot)
# Fine parte 1

# Inizio Parte 2
contatore = 3
sommaGruppi = 0
for i in range(len(righeFile)):
    for j in range(len(righeFile[i * contatore])):
        charAttuale = righeFile[i * contatore][j]
        if righeFile[i * contatore + 1].__contains__(charAttuale) and righeFile[i * contatore + 2].__contains__(charAttuale):
            if charAttuale.isupper():
                sommaGruppi += ord(charAttuale) - 38
                break
            else:
                sommaGruppi += ord(charAttuale) - 96
                break

print(sommaGruppi)
# Inizio parte 2



# gruppoDiTre = []
# listaDiGruppi = []
# contatore = 0
# for riga in righeFile:
#     if contatore % 3 != 0:
#         gruppoDiTre.append(riga)
#     else:
#         listaDiGruppi.append(gruppoDiTre)
#         gruppoDiTre.clear()
#         gruppoDiTre.append(riga)
#
#     contatore += 1
#
# sommaGruppi = 0
# for gruppo in listaDiGruppi:
#     for i in range(len(gruppo[0])):
#         charAttuale = gruppo[0][i]
#         if gruppo[1].__contains__(charAttuale) and gruppo[2].__contains__(charAttuale):
#             if charAttuale.isupper():
#                 sommaGruppi += ord(charAttuale) - 38
#                 break
#             else:
#                 sommaGruppi += ord(charAttuale) - 96
#                 break
#
#
#
# print(sommaGruppi)

