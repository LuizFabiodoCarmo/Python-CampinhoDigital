#calcular insulina

#store the human prepoinsulin sequence in a variable called prepoinsulin:

prepoInsulin = "malwrllpllallalwgpdpaaafvnghlcgshlvealylvcgergffytpktr" \
"reaedlqvggvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn"

#Store the remaining sequence elements of human insulin in variables:

#Variáveis com seus valores definidos
lsInsulin = "malwrllpllallalwgpdpaaa"
bInsulin = "fvnghlcgshlvealylvcgergffyt"
aInsulin = "giveqcctsicslyqlenycn"
cInsulin = "reaedlqvggvelgggpgagslqplalegslqkr"

#mostrando os valores das variáveis
print("A sequência da preproinsulina humana:")
print(prepoInsulin)

#sequência de insulina humana
insulin = bInsulin + aInsulin
print("Insulina humana:" + insulin)

#printing to console using concatenated strings inside the print function (one-liner):
print("the sequence of human insulin, chain b:"+ bInsulin)
print("the sequence of human insulin, chain a:"+ aInsulin)

#lista de aminoacidos e pesos
aaweights = {"A":89.09, "C":121.16, "D":133.10, "E":147.13, "F":165.19,
"G":75.07, "H":155.16, "I":131.17, "K":146.19, "L":131.17, "M":149.21,
"N":132.12, "P":115.13, "Q":146.15, "R":174.20, "S":105.09, "T":119.12,
"V":117.15, "W":204.23, "Y":181.19}
 
#Agora precisa fazer a contagem de cada aminoacido contido no dicionario acima
aaCountInsulin = ({x: float(insulin.upper().count(x)) for x in ['A','C',
'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R','S', 'T',
'V', 'W', 'Y']}) 

print("-----------------------")

#mostrar a contagem
print(aaCountInsulin)

#calcular e somar o total de valores dos pesos
molecularWeightInsulin = sum({x: (aaCountInsulin[x]*aaweights[x]) for x in
['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R',
 'S', 'T', 'V', 'W', 'Y']}.values()) 

#mostra o resultado
print("total do peso molecular da inulina:"+ str(molecularWeightInsulin))

#peso molecular padrão 
molecularWeightInsulinActual = 5807.63

#calcular o percentual de erro
print("Percentual de erro:" + str(((molecularWeightInsulin - molecularWeightInsulinActual)/molecularWeightInsulinActual)*100))

