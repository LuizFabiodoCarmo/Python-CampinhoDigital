#Aqui utilizamos o código de Cifra de Cesar já criado na aula do Dia-5, para fazer os testes de debugger na IDE Cloud 9.

#Assim como em outras IDEs, o Cloud 9 depura o código e aponta erros ou alertas contidos nele.

#Logo em seguida tivemos a tarefa de corrigir erros em códigos já criados, os erros eram apontados pelo debbuger do Cloud 9.
  #Os exercícios auxiliaram a compreender a importância de depurar um código pois ele nos aponta a linha em que o erro se encontra.
  



#Cifra de Cesar, criptografia antiga

# função para duplicar o alfabeto
def getDoubleAlphabet(alphabet):
    doubleAlphabet = alphabet + alphabet
    return doubleAlphabet

# função que solicita a mensagem a ser encriptada
def getMessage():
    stringToEncrypt = input("Por favor, digite a mensagem que será encriptada: ")
    return stringToEncrypt

# função que determina o número de chave para encriptar de 1 a 25
def getCipherKey():
    shiftAmount = input( "Please enter a key (whole number from 1-25): ")
    return shiftAmount

#função para encriptar a mensagem
def encryptMessage(message, cipherKey, alphabet):

    # iniciando as variaveis
    encryptedMessage = ""
    uppercaseMessage = ""

    # convertendo a mensagem para letras maiusculas
    uppercaseMessage = message.upper()

    # loop para percorrer cada caractere em uppercaseMessage
    for currentCharacter in uppercaseMessage:

        # percorre as letras do alfabeto
        # buscar posicao, ex: A = 0, B = 1...
        position = alphabet.find(currentCharacter)

        # gera uma nova posicao a partir da chave de cifra
        newPosition = position + int(cipherKey)

        # condicional
        # se a letra contem no alfabeto
        if currentCharacter in alphabet:
            encryptedMessage = encryptedMessage + alphabet[newPosition] # B == 1, CHAVE == 5 => 5 + 1 = 6 => G
        else:
            encryptedMessage = encryptedMessage + currentCharacter

    return encryptedMessage

#função para encriptar mensagem
def decryptMessage(message, cipherKey, alphabet):

    # retornar a posicao original
    # -1 inverte a posicao (do final para o inicio)
    decryptKey = -1 * int(cipherKey)

    # retorna a mensagem decriptada
    return encryptMessage(message, decryptKey, alphabet)



#função principal do programa de cifras de Cesar
def runCaesarCipherProgram():

    # definicao do alfabeto
    myAlphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    print(f'Alphabet: {myAlphabet}')

    # funcao com alfabeto duplicado
    myAlphabet2 = getDoubleAlphabet(myAlphabet)
    print(f'Alphabet2: {myAlphabet2}')

    # recuperar a mensagem do usuario
    myMessage = getMessage()
    print(myMessage)

    # recuperar a chave de cifra
    myCipherKey = getCipherKey()
    print(myCipherKey)

    # encriptar a mensagem
    myEncryptedMessage = encryptMessage(myMessage, myCipherKey, myAlphabet2)
    print(f'Encrypted Message: {myEncryptedMessage}')

    # decriptar a mensagem
    myDecryptedMessage = decryptMessage(myEncryptedMessage, myCipherKey, myAlphabet2)
    print(f'Decypted Message: {myDecryptedMessage}')

# executar a funcao principal
runCaesarCipherProgram()