# Abrir e ler o arquivo

import re
import os

with open('Dia-3/preinsulin-seq.txt') as file:
   
    #Criamos a váriavel insulinFile
    insulinFile = file.read()

#mostrar os dados lidos no arquivo
print("----DADO ORIGINAL----")  
print(insulinFile)      

#Criação de uma função para limpar os dados

def clean_text(string):
    # Agora tendo os dados recuperados, precisamos limpar o código, mantendo apenas o caracteres

    #Removendo o ORIGIN
    string = string.replace("ORIGIN", "")   
 
   #Removendo os números do código
    string = string.replace("61", "")

    string = string.replace("1", "")

    #removendo o //
    string = string.replace("//", "")

    #removendo os espaços em branco
    string = string.replace(" ", "")

    #removendo a quebra de linha \n
    string = string.replace("\n", "")

    #Retornar a string formatada
    return string

    #para limpar os dados criamos a variável cleanInsulin
cleanInsulin = clean_text(insulinFile)

#mostrando os dados limpos
print("----DADOS LIMPOS----")
print("cleanInsulin")

#Fazendo a contagem dos caracteres
print("-----COBTAGEM DE CARACTERES-----")
print("Quantidade de caracteres: {}",format(len(cleanInsulin)))



  
   





    


