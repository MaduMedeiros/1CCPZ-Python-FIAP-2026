lista_frutas = ["banana", "maça", "morango"]

print(lista_frutas[1])

lista_frutas.append("uva")#append adiciona um na lista
print(lista_frutas[-1])#-1 vem do tamanho da array -1

tamanho = len(lista_frutas)
print(tamanho)

for i in range(tamanho): #aq eu acesso pelo índice
    print(lista_frutas[i])

for fruta in lista_frutas:#aq eu acesso direto
    print(fruta)

msg = "oi fulano!" #str tbm é array

for i in range(len(msg)):
    print(msg[i])