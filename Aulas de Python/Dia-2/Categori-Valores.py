'''Categorização de valores
No Python, você pode misturar os tipos de uma lista. Neste laboratório, você criará uma lista com diferentes tipos e acessará os valores.'''

# Criação de lista com tipos de dados mistos.
MyListaMista = [13, 220793, 1.88, True, "Eu adoro programar", "45"]
#estrutura de repetição/loop
for item in MyListaMista:
    print("{} é um tipo de dado {}".format(item,type(item)))