# Subscriber 2

#   Importando a biblioteca do Socket
import socket

#   Definindo meu Host e porta
HOST = 'localhost'
PORT = 5002

#   Criando o objeto socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print('\nConectando.......\n')

#   Pedindo a conexao ao Broker
s.connect((HOST, PORT))

print('Conexão concluida!\n')

#   Lista de inscrições do Subscriber
inscricoes = ['']



def Inscrição():
    #   Recebendo a lista de Publishers
    cont = 0
    Publishers = []
    while cont < (3):
        value = s.recv(1024)
        Publishers.append(value.decode())
        cont += 1

    #   Imprimindo a lista de Publishers para o Subscriber escolher:
    print('\nPublishers cadastrados:')
    for n in Publishers:
        print('->',n)

    #   Perguntar oa Subscriber qual Publisher ele quer se inscrever
    print('Qual Publisher voce quer se inscrever?')
    resposta = input()

    #   Envia a resposta
    print('\nInscrição concluida em: ', resposta)
    s.sendall(str.encode(resposta))


#   Função responsavel por receber a mensagem do Broker


def RecebeMensagem():
    i = 0
    numEscricao = s.recv(1024)
    while i < int(numEscricao):
        i = i+1
        #   Recebendo resposta da comunicacao
        data = s.recv(1024)
        print('\nMensagem recebida: ', data.decode(), '\n')

#   Função responsavel por enviar a requisição de desinscrição do Publisher


def Desinscrever():
    numinscricoes = s.recv(1024)
    cont = 0
    while cont < (int(numinscricoes.decode())):
        value = s.recv(1024)
        inscricoes.append(value.decode())
        cont += 1

    #   Imprimindo a lista:
    print('\nVocê está inscrito nos Publichers:')
    for n in inscricoes:
        print(n)

    #   Perguntar oa usuario qual Publisher ele quer se desinscrever
    print('\nQual Publisher voce quer se desinscrever?')
    resposta = input()

    #   Envia a resposta
    print('\nDesinscrito do Publisher: ', resposta, '\n')
    s.sendall(str.encode(resposta))

    #   Limpa a lista aqui para receber uma nova lista atualizada do Broker
    inscricoes.clear()


# Rotina de execução do Subscriber
while True:

    #   Lendo opção que o Subscriber deseja fazer:
    print('\n----Menu Subscribe 2----\n')
    print('Digite 1 para receber mensagens')
    print('Digite 2 para se inscrever')
    print('Digite 3 para se desinscrever')
    print('Digite 4 para sair')
    opcao = input()
    #   Comunica o Broker da intenção do Subscriber
    s.sendall(str.encode(opcao))
    # Executa as funç~eos de acordo com o escolhido pelo Subscriber
    if (opcao == '1'):
        RecebeMensagem()
    elif (opcao == '2'):
        Inscrição()
    elif (opcao == '3'):
        Desinscrever()
    else:
        s.close()
        break
