from socket import socket, AF_INET, SOCK_DGRAM, timeout
# importo ciò che mi serve dalla libreria socket

serverName = "197.247.242.1"
# tradotto con indirizzo di loopback 127.0.0.1
serverPort = 12001
# porte fino alla 1024 sono registrate
bufferSize = 2048
timeLimit = 1

clientSocket = socket(AF_INET, SOCK_DGRAM)
# AF_INET -> sto usando indirizzi IPV4, AF_INET6
# 2 argomento -> tipo di socket che sto creando
#   SOCK_DGRAM -> UDP
#   SOCK_STREAM -> TCP
message = input(f"➡️ Inserire il messaggio: ")
indirizzo = (serverName, serverPort)

clientSocket.settimeout(timeLimit)

clientSocket.sendto(message.encode("utf-8"), indirizzo)

try:
    modifiedMessage, serverAddress = clientSocket.recvfrom(bufferSize)
    # bloccante, prende per argomento la dimensione del buffer di ricezione
    # ritorna ServerAddress, tupla simile ad indirizzo
    print(f"✔️ Il messaggio modificato: {modifiedMessage.decode('utf-8')}\n")

except timeout:
    print(f"❌ Timeout di scaduto di {timeLimit} second{'o' if timeLimit==1 else 'i'}, server non raggiungibile")

finally:
    clientSocket.close()
    clientSocket.close

