#Módulo personalizado para ler arquivo JSON

# importar o modulo JSON
import json

# função com tratamento de excessão try/except
def readJsonFile(fileName):
    data = ""

    # estrutura com tratamento de excessão
    # tente executar a leitura do arquivo JSON
    try:
        with open(fileName) as json_file:
            data = json.load(json_file)

    # caso nao consiga
    # mostre a mensagem de erro de leitura
    except IOError:
        print("Could not read file")
    
    # retorna o conteudo do arquivo
    return data

 #ler o arquivo
#file = readJsonFile("Dia-5\insulin.json")
#print('JSON: {}'.format(file))