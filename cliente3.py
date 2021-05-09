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

#   Lista de inscrições do usuario
inscricoes1 = ['']

#   Contador de quantas inscrições o Inscrito tem
global contInscri
contInscri = 0


def Inscrição(contInscri):
    contInscri = contInscri+1
    #   Recebendo a lista de Publichers
    listaPub1 = s.recv(1024)
    listaPub2 = s.recv(1024)
    listaPub3 = s.recv(1024)

    #   Imprimindo a lista:
    print('\nPublishers cadastrados:')
    print('->', listaPub1.decode())
    print('->', listaPub2.decode())
    print('->', listaPub3.decode())

    #   Perguntar oa usuario qual publisher ele quer se inscrever
    print('Qual Publisher Voce que se inscrever?')
    resposta = input()

    #   Envia a resposta
    print('\nInscrição concluida em: ', resposta)
    s.sendall(str.encode(resposta))
    return contInscri


def RecebeMensagem(contInscri):
    i = 0
    while i < contInscri:
        i = i+1
        #   Recebendo resposta da comunicacao
        data = s.recv(1024)
        print('\nMensagem recebida: ', data.decode(), '\n')


def Desinscrever(contInscri):
    contInscri = contInscri-1
    numInscricoes1 = s.recv(1024)
    cont = 0
    while cont < (int(numInscricoes1.decode())):
        inscricoes1.append(s.recv(1024))
        cont += 1

    #   Imprimindo a lista:
    print('\nInscritos nos Publichers:')
    for n in inscricoes1:
        print(n)

    #   Perguntar oa usuario qual publisher ele quer se desinscrever
    print('\nQual Publisher Voce que se desinscrever?')
    resposta = input()

    #   Envia a resposta
    print('\nDesinscrito em: ', resposta, '\n')
    s.sendall(str.encode(resposta))

    #   Limpa a lista aqui para receber uma nova lista atualizada do servidor
    inscricoes1.clear()
    return contInscri


while True:

    #   Lendo opção que o cliente quer fazer
    print('\n----Menu----\n')
    print('Digite 1 para receber mensagens')
    print('Digite 2 para se inscrever')
    print('Digite 3 para se desinscrever')
    print('Digite 4 para sair')
    opcao = input()

    s.sendall(str.encode(opcao))

    if (opcao == '1'):
        RecebeMensagem(contInscri)  
    elif (opcao == '2'):
        contInscri = Inscrição(contInscri)
    elif (opcao == '3'):
        contInscri = Desinscrever(contInscri)
        
    else:
        s.close()
        break
