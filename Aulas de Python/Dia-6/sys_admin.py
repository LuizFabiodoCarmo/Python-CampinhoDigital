#Utilizando o modo OS na IDE Cloud 9

 #Importando o módulo
import os
import subprocess


#Retorna a lsitagem da pasta
#Utilizando o .system()
print("-----OS SYSTEM-----")
os.system("ls")

print("-----OS SYSTEM-----")
# #Utilizando o subprocess
# #quando mandamos rodar o "ls", lista todas as pastas dentro do diretório "Aulas Python"
subprocess.run(["ls"])

#Retornar arquivos e pastas com infos
print("-----DETALHES-----")
subprocess.run(["ls","-l"])
#Retornar informação de arquivo específico 
print("-----ESPECÍFICO-----")
subprocess.run(('ls','-l', "README.md"))

#Executar comando armazenados em variáveis 

#Variáveis
command = "uname"
commandArgument = "a"

#Mensagem informativa
print(f'Gathering system information with command: (command) {commandArgument}')

#Executar
subprocess.run([command, commandArgument])

command = 'ps'
commandArgument = '-x'
print(f'Gathering active process information with command: (command) {commandArgument}')
subprocess.run([command, commandArgument])