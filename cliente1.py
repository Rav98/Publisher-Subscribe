# Subscriber 1

#   Importando a biblioteca do Socket
import socket

#   Importando biblioteca de matematica para o calculo
import math

#   Definindo meu Host e porta
HOST = 'localhost'
PORT = 5001

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
        print('->', n)

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


#   Recebe os calculos e processa ele
def RecebeCalculo():
    i = 0
    numEscricao = s.recv(1024)
    while i < int(numEscricao):
        i = i+1
        #   Recebendo resposta da comunicacao
        data = s.recv(1024)
        funcao = s.recv(1024)
        print('\nCalculo Recebido: ', data.decode(), '\n')
        print('Calculando......')
        #   Calcula Diametro
        if(funcao.decode() == '1'):
            diametro = 2*int(data.decode())
            print('Calculo do Diametro da Circunferencia executado, valor= ', diametro)
        #   Calcula da Área
        elif(funcao.decode() == '2'):
            area = math.pi*int(data.decode())
            print('Calculo da Area da Circunferencia executado, valor= ', area)
        #   Calcula da Comprimento
        elif(funcao.decode() == '3'):
            comprimento = 2*math.pi*int(data.decode())
            print(
                'Calculo do Comprimento da Circunferencia executado, valor= ', comprimento)

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
    print('\n----Menu Subscribe 1----\n')
    print('Digite 1 para receber mensagens')
    print('Digite 2 para receber calculos')
    print('Digite 3 para se inscrever para receber mensagens')
    print('Digite 4 para se inscrever para receber calculos')
    print('Digite 5 para se desinscrever')
    print('Digite 6 para sair')
    opcao = input()
    #   Comunica o Broker da intenção do Subscriber
    s.sendall(str.encode(opcao))
    # Executa as funç~eos de acordo com o escolhido pelo Subscriber
    if(opcao == '1'):
        RecebeMensagem()
    elif(opcao == '2'):
        RecebeCalculo()
    elif(opcao == '3'):
        Inscrição()
    elif(opcao == '4'):
        Inscrição()
    elif(opcao == '5'):
        Desinscrever()
    else:
        s.close()
        break
