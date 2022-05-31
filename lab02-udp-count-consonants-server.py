from socket import socket, AF_INET, SOCK_DGRAM

vowels = {"a", "e", "i", "o", "u"}

def isAlpha(char):
    return char >= 'a' and char <='z'

def elaborate(string):
    consonants = 0
    for char in string.lower():
        if char not in vowels and isAlpha(char):
            consonants += 1
    return consonants


serverPort = 12000
bufferSize = 2048

serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(("", serverPort))
# opera sulla porta serverPort
# bind vuole tupla (indirizzo, porta) se indirizzo == "" -> locale

print("Server Up and Running ☑️")

while True:
    #Server deve girare in background
    message, clientAddress = serverSocket.recvfrom(bufferSize)
    # mi segno il messaggio e la tupla con indirizzo e porta del client
    print(f"➡ Ricevuto da ({clientAddress[0]}:{clientAddress[1]}): {message.decode('utf-8')}")
    message = message.decode("utf-8")
    modified_message = str(elaborate(message))
    #   e' inportante fare il casting
    serverSocket.sendto(modified_message.encode("utf-8"), clientAddress)

serverSocket.close()