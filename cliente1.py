# Cliente 1 

#   Importando o socket
import socket

#   Definindo meu Host e porta 
HOST='localhost'
PORT=5001

#   Criando o objeto socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#   Pedindo a conexao ao servidor
s.connect((HOST,PORT))

#   Recebendo resposta da comunicacao 
data=s.recv(1024)
print(data.decode())