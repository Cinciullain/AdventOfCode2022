with open("calorieElfi.txt", "r") as file:
    righeFile = file.readlines()

for i in range(len(righeFile)):
    if righeFile[i].endswith("\n"):
        righeFile[i] = righeFile[i][:-1]

elfoAttuale = 0
listaElfi = []

for x in range(len(righeFile)):
    if righeFile[x] != '':
        elfoAttuale = elfoAttuale + int(righeFile[x])

    else:
        listaElfi.append(elfoAttuale)
        elfoAttuale = 0

#Star 1
print(max(listaElfi))
listaElfi.sort(reverse=True)
#Star 2
print(sum(listaElfi[:3]))

