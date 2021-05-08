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

def Incrição()
    #   Recebendo a lista de Publichers
    listaPub1 = s.recv(1024)
    listaPub2 = s.recv(1024)
    listaPub3 = s.recv(1024)

    #   Imprimindo a lista:
    print('\nPublishers cadastrados:')
    print(listaPub1.decode())
    print(listaPub2.decode())
    print(listaPub3.decode())
    print('\n')

    #   Perguntar oa usuario qual publisher ele quer se inscrever
    print('Qual Publisher Voce que se inscrever?')
    resposta = input()

    #   Envia a resposta
    print('Inscrição concluida em: ', resposta)
    s.sendall(str.encode(resposta))

def RecebeMensagem()

    #   Recebendo resposta da comunicacao
    data = s.recv(1024)
    print('\nMensagem recebida: ', data.decode())

def Desiscrever()

    


while True:
    Incrição()
    RecebeMensagem()



