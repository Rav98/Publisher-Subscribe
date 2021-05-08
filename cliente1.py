# Cliente 1

#   Importando o socket
import socket

#   Definindo meu Host e porta
HOST = 'localhost'
PORT = 5001

#   Criando o objeto socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#   Pedindo a conexao ao servidor
s.connect((HOST, PORT))

#   Recebendo a lista de Publichers
listaPub1 = s.recv(1024)
listaPub2 = s.recv(1024)
listaPub3 = s.recv(1024)
print('Publishers cadastrados:')
print(listaPub1.decode())
print(listaPub2.decode())
print(listaPub3.decode())

#   perguntar oa usuario qual publisher ele quer se inscrever
print('Qual Publisher Voce que se inscrever?')
resposta = input()

#   envia a resposta
print('Resposta enviada: ', resposta)
s.sendall(str.encode(resposta))

#   Recebendo resposta da comunicacao
data = s.recv(1024)
print('Resposta recebida:', data.decode())
