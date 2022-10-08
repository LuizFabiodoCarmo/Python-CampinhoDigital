'''Uso de loops'''

#importando módulo random.
import random



#mostrar mensagem de boas vindas com as regras.
print("Welcome to Guess the Number!")
print("The rules are simple. I will think of a number, and you will try to guess it.")

#gera um número randômico de 1 a 10.
number = random.randint(1,10)

print(number)

#váriavel de controle.
isGuessRight = False

#loop.
while isGuessRight != True:
    #pode que o usuário digite um número de 1 a 10.
    guess = input("Guess a number between 1 and 10: ")
    
    #condicional que verifica se o número é o correto.
    if int(guess) == number:
        print("You guessed {}. That is correct! You win!".format(guess))
        #altera a variável de controle.
        isGuessRight = True
    #caso o número não seja adivinhado.
    else:
        print("You guessed {}. Sorry, that isn’t it. Try again.".format(guess))
        
        
        
        
        
        
        
        
        