from socket import socket, AF_INET, SOCK_DGRAM

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
    modified_message = message.upper()
    serverSocket.sendto(modified_message.encode("utf-8"), clientAddress)

serverSocket.close()