'''Condicionais'''

#recuperar informações do usuário.
userReply = input("Você precisa enviar algo? (Enter yes or no) ")

#condicional com If(se)
if userReply == "yes":
    print("Legal, nós podemos enviar o pacote!")
elif userReply == "no":
    print("Tudo bem, obrigada!")
else:
    print("Esse comando não é válido, por favor, dê play novamente e digite yes ou no!")
    
'''if int(userReply) != "yes" or "no":
    print("Vamos tentar outra vez, você precisa enviar algo?".format(userReply))
    
    Acho que pra isso funcionar, eu teria que declarar "yes" e "no" como valores de uma outra váriavel, para aí sim funcionar o loop que leva
       para a pergunta inicial.
 '''  
    

    