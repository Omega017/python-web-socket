from socket import *

serverName = 'localhost'
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_DGRAM)

sum = raw_input('Input the sum (e.g: 2+2): ')

clientSocket.sendto(sum, (serverName, serverPort))

numbersAdd, serverAddress = clientSocket.recvfrom(2048)

print numbersAdd

clientSocket.close()
