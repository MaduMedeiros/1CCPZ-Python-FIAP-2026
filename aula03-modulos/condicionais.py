from streamlit import login
from sympy import false

idade = 20

maior_idade = idade >= 18
print(maior_idade, type (maior_idade))
#operadones lógicos: or, and, not

#lógica and

print() #pula uma linha

verifica_email = True
verifica_senha = False

login = verifica_email and verifica_senha
print(login)

#if login:
 #   print("entrar no sistema")

if not login: #if not é lógica inversa
    print("burrao leso acerta essa senha mano")


print()
#notas

nota_final = 7

#if nota_final < 4:
#    print("reprovado")
#else:
#   if nota_final < 6:
#        print("recuperação")
#    else:
#        print("aprovado")

if nota_final < 4:
    print("reprovado")

elif nota_final < 6:
    print("recuperação")
else:
    print("aprovado")

print("fim")