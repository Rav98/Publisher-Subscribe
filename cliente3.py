# Cliente 3

#   Importando o socket
import socket

#   Definindo meu Host e porta
HOST = 'localhost'
PORT = 5003

#   Criando o objeto socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print('Conectando.......\n')

#   Pedindo a conexao ao servidor
s.connect((HOST, PORT))

print('Conexão concluida!\n')


def Inscrição():
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


def RecebeMensagem():
    #   Recebendo resposta da comunicacao
    data = s.recv(1024)
    print('\nMensagem recebida: ', data.decode())


while True:

    #   Lendo opção que o cliente quer fazer
    print('----Menu----\n')
    print('Digite 1 para receber mensagens')
    print('Digite 2 para se inscrever')
    print('Digite 3 para se desinscrever')
    print('Digite 4 para sair')
    opcao = input()

    s.sendall(str.encode(opcao))

    if (opcao == '1'):
        RecebeMensagem()
    elif (opcao == '2'):
        Inscrição()
    elif (opcao == '3'):
        print('desinscrevendo')
    else:
        break
   
