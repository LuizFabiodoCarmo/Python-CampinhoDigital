#Carregando insulina

#store the human prepoinsulin sequence in a variable called prepoinsulin:

prepoInsulin = "malwrllpllallalwgpdpaaafvnghlcgshlvealylvcgergffytpktrreaedlqvggvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn"

#Store the remaining sequence elements of human insulin in variables:

lsInsulin ="malwmrllpllallalwgpdpaaa"
bInsulin = "fvnqhlcgshlvealylvcgergffytpkt"
aInsulin = "giveqcctsicslyqlenycn"
cInsulin = "rreaedlqvgqvelgggpgagslqplalegslqkr"
insulin = bInsulin + aInsulin

pkR = {'y':10.07, 'c':8.18, 'k':10.53,'h':6.00,'r':12.48,'d':3.65,'e':4.25}

seqCount = ({x: float(insulin.count(x))for x in ['y','c','k','h','r','d','e']})

print(seqCount)

#---------------------------

pH = 0

while (pH <= 14):
        netCharge =(
        +(sum({x: ((seqCount [x]*(10**pkR[x]))/((10**pH)+(10**pkR[x]))) \
        for x in ['k','h','r']}.values()))
        -(sum({x: ((seqCount [x]*(10**pH))/((10**pH)+(10**pkR[x]))) \
        for x in ['y','c','d','e']}.values())))      

        #mostra o resultado   
        print("{0:.2f}".format(pH), netCharge)

        #Incrementar variável de controle
        pH +=1 