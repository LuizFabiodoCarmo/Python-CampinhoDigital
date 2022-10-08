'''Tipos de dados String'''

#multiplas váriaveis.
myName = "Luiz"
myLastname = "Fabio"
myAge = "29" 
# caso queira o número sem aspas, deve se fazer o tratamento dele na linha do código abaixo, "str(myAge)"."

# mostra informações de forma organizada.
print("Meu nome é : " + myName +  " " + myLastname + ", tenho " + myAge + " anos,")

#String de entrada com input
myName = input("Qual é seu nome?")
myLastname = input("Qual é seu sobrenome?")
myAge = input("Qual é sua idade?") 
#input entra como String.

print("Meu nome é : " + myName +  " " + myLastname + ", tenho " + myAge + " anos,")

#String de saída com format
print("Meu nome é : {} {}, tenho {} anos." .format(myName, myLastname, myAge))

