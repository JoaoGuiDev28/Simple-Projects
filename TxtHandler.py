pessoas = list()
media = list()
p = list()
num = list()
final = dict()
sum = 0
f = 0

nomes = open('arq1.txt', 'r')
pessoas = nomes.readlines()
nomes.close()

nota = open('arq2.txt', 'r')
media = nota.readlines()
nota.close()

for f in range(0, len(media)):
    p = pessoas[f].replace('\n', '')
    num = media[f].split(',')
    sum = (float(num[0]) + float(num[1])) / 2

    final[f] = f"{p} , {round(sum, 2)} \n"


with open('arq3.txt', 'w') as geral:
    for f in range(0, len(media)):
        geral.write(final[f])

geral.close()