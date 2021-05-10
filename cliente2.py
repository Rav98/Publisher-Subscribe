# Subscriber 2

#   Importando a biblioteca do Socket
import socket

#   Definindo meu Host e porta
HOST = 'localhost'
PORT = 5002

#   Criando o objeto socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print('Conectando.......\n')

#   Pedindo a conexao ao Broker
s.connect((HOST, PORT))

print('Conexão concluida!\n')

#   Lista de inscrições do Subscriber
inscricoes = ['']

#   Contador de quantas inscrições o Subscriber tem
global contInscri
contInscri = 0


def Inscrição(contInscri):
    contInscri = contInscri+1
    #   Recebendo a lista de Publishers
    Pub1 = s.recv(1024)
    Pub2 = s.recv(1024)
    Pub3 = s.recv(1024)

    #   Imprimindo a lista de Publishers para o Subscriber escolher:
    print('\nPublishers cadastrados:')
    print('->', Pub1.decode())
    print('->', Pub2.decode())
    print('->', Pub3.decode())

    #   Perguntar oa Subscriber qual Publisher ele quer se inscrever
    print('Qual Publisher Voce que se inscrever?')
    resposta = input()

    #   Envia a resposta
    print('\nInscrição concluida em: ', resposta)
    s.sendall(str.encode(resposta))
    return contInscri

#   Função responsavel por receber a mensagem do Broker


def RecebeMensagem(contInscri):
    i = 0
    while i < contInscri:
        i = i+1
        #   Recebendo resposta da comunicacao
        data = s.recv(1024)
        print('\nMensagem recebida: ', data.decode(), '\n')

#   Função responsavel por enviar a requisição de desinscrição do Publisher


def Desinscrever(contInscri):
    contInscri = contInscri-1
    numinscricoes = s.recv(1024)
    cont = 0
    while cont < (int(numinscricoes.decode())):
        inscricoes.append(s.recv(1024))
        cont += 1

    #   Imprimindo a lista:
    print('\nInscritos nos Publichers:')
    for n in inscricoes:
        print(n)

    #   Perguntar oa usuario qual Publisher ele quer se desinscrever
    print('\nQual Publisher Voce que se desinscrever?')
    resposta = input()

    #   Envia a resposta
    print('\nDesinscrito em: ', resposta, '\n')
    s.sendall(str.encode(resposta))

    #   Limpa a lista aqui para receber uma nova lista atualizada do Broker
    inscricoes.clear()
    return contInscri


# Rotina de execução do Subscriber
while True:

    #   Lendo opção que o Subscriber deseja fazer:
    print('\n----Menu----\n')
    print('Digite 1 para receber mensagens')
    print('Digite 2 para se inscrever')
    print('Digite 3 para se desinscrever')
    print('Digite 4 para sair')
    opcao = input()
    #   Comunica o Broker da intenção do Subscriber
    s.sendall(str.encode(opcao))
    # Executa as funç~eos de acordo com o escolhido pelo Subscriber
    if (opcao == '1'):
        RecebeMensagem(contInscri)
    elif (opcao == '2'):
        contInscri = Inscrição(contInscri)
    elif (opcao == '3'):
        contInscri = Desinscrever(contInscri)
    else:
        s.close()
        break
