#calculo de média  porem força o usuário a ser gente, validação
def validar_nota(nota):
    while  nota < 0 or nota > 10:
        print("a nota deve estar entre zero  e dez")
        nota = float(input("Digite a nota novamente:"))
    return nota

notaA = float(input("Digite a primeira nota:"))
notaA = validar_nota(notaA)


notaB = float(input("Digite a segunda nota"))
notaB = validar_nota(notaB)

#pode ser assim, sem a função:
# while  notaB < 0 or notaB > 10:          o notaA tava assim tbm mas mudamos pra ficar melhor
#     print("a nota deve estar entre zero  e dez")
#     notaB = float(input("Digite a segunda nota novamente:"))

media = (notaA + notaB) / 2
print(media)