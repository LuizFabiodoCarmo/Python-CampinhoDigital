'''Um tipo de dado composto é todo tipo de dado que seja formado por tipos de dados primitivos.'''
#Código para ler arquivo CSV.

#importando módulos
import csv
import copy

#criando dicionário que funcionará como tipo composto para a leitura dos dados tabulares.
myVehicle = {
    "vin" : "<empty>",
    "make" : "<empty>" ,
    "model" : "<empty>" ,
    "year" : 0,
    "range" : 0,
    "topSpeed" : 0,
    "zeroSixty" : 0.0,
    "mileage" : 0
}
#estrutura de repetição/loop.
for chave, valor in myVehicle.items():
    print("{} : {}".format(chave,valor))
    #print(chave + ":" + str(valor))
    
#criar lista de inventário vazia.
myInventoryList = []

#ler arquivo CSV
with open('Dia-2/car_fleet.csv') as csvFile:
#car_fleet.csv é o nome do arquivo, seria uma abreviação/apelido para ele.

    # csvReader, recebe dois parâmetros, 1º o arquivo para leitura(csvFile), 2º o delimitador(delimiter=',') que seria a vírgula.
    csvReader = csv.reader(csvFile, delimiter=',')  
    
    #variável de controle.
    lineCount = 0  
    
    #estrutura de repetição.
    for row in csvReader:
        #condicional para recuperar os nomes das colunas.
        if lineCount == 0:
            #interpolação de expressões.
            print(f'Column names are: {", ".join(row)}') 
            
            #incrementar a variavel de controle +1.
            lineCount += 1  
            
        else:  
            #mostra os valores das linhas, maiores que zero.
            print(
            f'vin: {row[0]}\n'
            f'make: {row[1]}\n'
            f'model: {row[2]}\n'
            f' year: {row[3]}\n'
            f' range: {row[4]}\n'
            f' topSpeed: {row[5]}\n'
            f' zeroSixty: {row[6]}\n'
            f' mileage: {row[7]}\n'
            )  
            
            #criar cópia dos dados lídos.
            currentVehicle = copy.deepcopy(myVehicle) 
            
            #acessa as posições da lista e atribui os valores.
            currentVehicle["vin"] = row[0]  
            currentVehicle["make"] = row[1]  
            currentVehicle["model"] = row[2]  
            currentVehicle["year"] = row[3]  
            currentVehicle["range"] = row[4]  
            currentVehicle["topSpeed"] = row[5]  
            currentVehicle["zeroSixty"] = row[6]  
            currentVehicle["mileage"] = row[7]  
            
            #adiciona os dados na lista vazia.
            myInventoryList.append(currentVehicle) 
            
            #incrementa a váriavel de controle.
            lineCount += 1  
            
     #mostra a quantidade de linhas processadas.       
    print(f'Processed {lineCount} lines.')
    
    for myCarProperties in myInventoryList:
        
        #tupla de dados: chave, valor.
       for chave, valor in myCarProperties.items():
          print("{} : {}".format(chave,valor))
          print("-----")
    
    
    
    
    
    
    
    
    