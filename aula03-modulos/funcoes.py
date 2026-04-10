from mypyc.ir.func_ir import num_bitmap_args


def print_lyrics():
    print("I ain't gonna live live forever")
    print("I just wanna live while I'm alive")
    print("It's my life")

print_lyrics()

def boas_vindas(nome):
    print(f"olá, {nome}!! seja bem-vindo!") #f aqui ta substituindo e formantando o {nome} pelo nome q eu digitar

nome_digitado = input("Digite seu nome:")
boas_vindas(nome_digitado)

#até agora ta sem retorno

def soma (num_a, num_b):
    soma = num_a + num_b
    return soma

resultado = (soma(7, 5))
print(resultado)
print(type(nome_digitado)) #type aqui está printando o tipo (literalmente tipo) doq eu coloquei pra printar