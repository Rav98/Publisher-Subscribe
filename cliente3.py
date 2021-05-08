# Cliente 3

#   Importando o socket
import socket

#   Definindo meu Host e porta
HOST = 'localhost'
PORT = 5003

#   Criando o objeto socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#   Pedindo a conexao ao servidor
s.connect((HOST, PORT))

#   Recebendo a lista de Publichers
listaPub1 = s.recv(1024)
listaPub2 = s.recv(1024)
listaPub3 = s.recv(1024)

# Imprimindo a lista:
print('\nPublishers cadastrados:')
print(listaPub1.decode())
print(listaPub2.decode())
print(listaPub3.decode())
print('\n')

#   perguntar oa usuario qual publisher ele quer se inscrever
print('Qual Publisher Voce que se inscrever?')
resposta = input()

#   envia a resposta
print('Inscrito em: ', resposta)
s.sendall(str.encode(resposta))

while True:
    #   Recebendo resposta da comunicacao
    data = s.recv(1024)
    print('\nMensagem recebida: ', data.decode())

    print('MENU:\n\n')
    print('(1) Continuar inscrito')
    print('(2) Se desinscrever')
    print('(3) Sair')
    opcao = input()

    if opcao == 1:
        s.sendall(str.encode('false'))

    elif opcao == 2:
        s.sendall(str.encode('true'))
