from socket import *

serverPort = 12000

serverSocket = socket(AF_INET, SOCK_DGRAM)

serverSocket.bind(('', serverPort))

print "The server is ready to receive"

while 1:
    sum, clientAddress = serverSocket.recvfrom(2048)

    numbers = sum.split('+')

    numbersAdd = str(int(numbers[0]) + int(numbers[1]))

    serverSocket.sendto(numbersAdd, clientAddress)
