#   Importando a biblioteca do Socket
import socket

#   Importando a biblioteca do PyPubSub
from pubsub import pub

#   Definindo meu Host e Porta
HOST = 'localhost'
PORT1 = 5001
PORT2 = 5002
PORT3 = 5003

#   Lista de Publichers cadastrados no sistema
listaPub = ['Futebol', 'Vôlei', 'Basquete']

#   Lista para salvar as inscrições de cada Subscriber
global ListaInscricaoPub1
ListaInscricaoPub1 = []
global listaInscricaoPub2
listaInscricaoPub2 = []
global listaInscricaoPub3
listaInscricaoPub3 = []

#   Variaveis globais para salvar as respostas retornadas pelos Subscribers
global RespSub1
global RespSub2
global RespSub3

#   Criando o objeto socket para cada inscrito
sub1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sub2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sub3 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#   Vincular servidor e porta oa socket
sub1.bind((HOST, PORT1))
sub2.bind((HOST, PORT2))
sub3.bind((HOST, PORT3))

#   Colocando o socket em modo de escuta
sub1.listen()
print('Aguardando conexao do sub1')

sub2.listen()
print('Aguardando conexao do sub2')

sub3.listen()
print('Aguardando conexao do sub3')

#   Retorno da confirmação da conexão pelo Subscriber
connexao1, endereco1 = sub1.accept()
print('Conectado com: ', endereco1)

connexao2, endereco2 = sub2.accept()
print('Conectado com: ', endereco2)

connexao3, endereco3 = sub3.accept()
print('Conectado com: ', endereco3)

#   Função que envia dados para os Subscribers inscritos


def sub1(data):
    connexao1.sendall(str.encode(data))


def sub2(data):
    connexao2.sendall(str.encode(data))


def sub3(data):
    connexao3.sendall(str.encode(data))


# Função responsavel por inscrever o usuario em algum Publisher
def Inscrição(sub):
    if(sub == '1'):
        # Envia a lista de Publishers:
        for n in listaPub:
            connexao1.sendall(str.encode(n))
        # Recebe Publisher escolhido pelo usuario
        RespSub1 = connexao1.recv(1024)
        ListaInscricaoPub1.append(RespSub1.decode())
        # imprime a escolha do usuario
        print('sub1 escolheu se inscrever em:', RespSub1.decode())
        #   Função responsavel por inscrever os Subscriber nos grupos
        pub.Subscriber(sub1, RespSub1.decode())

    elif(sub == '2'):
        # Envia a lista de Publishers:
        for n in listaPub:
            connexao2.sendall(str.encode(n))
        # Recebe Publisher escolhido pelo usuario
        RespSub2 = connexao2.recv(1024)
        listaInscricaoPub2.append(RespSub2.decode())
        # imprime a escolha do usuario
        print('sub2 escolheu se inscrever em:', RespSub2.decode())
        #   Função responsavel por inscrever os Subscribers nos grupos
        pub.Subscriber(sub2, RespSub2.decode())

    elif(sub == '3'):
        # Envia a lista de Publishers:
        for n in listaPub:
            connexao3.sendall(str.encode(n))
        # Recebe Publisher escolhido pelo usuario
        RespSub3 = connexao3.recv(1024)
        listaInscricaoPub3.append(RespSub3.decode())
        # imprime a escolha do usuario
        print('sub3 escolheu se inscrever em:', RespSub3.decode())
        #   Função responsavel por inscrever os Subscribers nos grupos
        pub.Subscriber(sub3, RespSub3.decode())

# Função responsavel por enviar a mensagem para cada Subscribers


def EnviarMensagem():
    #   Escolha da mensagem que se quer enviar
    print('\nEscreva uma mensagem para os Inscritos em:', listaPub[0])
    data1 = input()
    pub.sendMessage(listaPub[0], data=data1)
    print('\nEscreva uma mensagem para os Inscritos em:', listaPub[1])
    data2 = input()
    pub.sendMessage(listaPub[1], data=data2)
    print('\nEscreva uma mensagem para os Inscritos em:', listaPub[2])
    data3 = input()
    pub.sendMessage(listaPub[2], data=data3)
    print('\nMensagem enviada aos Subscribers!\n')

# Função responsavel por desinscrever o Subscriber


def Desinscrever(sub):
    if (sub == '1'):
        connexao1.sendall(str.encode(str(len(ListaInscricaoPub1))))
        for n in ListaInscricaoPub1:
            connexao1.sendall(str.encode(n))
        RespSub1 = connexao1.recv(1024)
        ListaInscricaoPub1.remove(RespSub1.decode())
        pub.unSubscriber(sub1, RespSub1.decode())
        print('sub1 se desinscreveu de:', RespSub1.decode())
    elif (sub == '2'):
        connexao2.sendall(str.encode(str(len(listaInscricaoPub2))))
        for n in listaInscricaoPub2:
            connexao2.sendall(str.encode(n))
        RespSub2 = connexao2.recv(1024)
        listaInscricaoPub2.remove(RespSub2.decode())
        pub.unSubscriber(sub2, RespSub2.decode())
        print('sub2 se desinscreveu de:', RespSub2.decode())
    elif (sub == '3'):
        connexao3.sendall(str.encode(str(len(listaInscricaoPub3))))
        for n in listaInscricaoPub3:
            connexao3.sendall(str.encode(n))
        RespSub3 = connexao3.recv(1024)
        listaInscricaoPub3.remove(RespSub3.decode())
        pub.unSubscriber(sub3, RespSub3.decode())
        print('sub3 se desinscreveu de:', RespSub3.decode())


# Rotina de execução do servidor.
while True:
    # ouvindo os Subscribers para saber se eles querem se inscrever ou desinscrever
    resposta1 = connexao1.recv(1024)
    if resposta1.decode() == '1':
        EnviarMensagem()
    elif resposta1.decode() == '2':
        Inscrição('1')
    elif resposta1.decode() == '3':
        Desinscrever('1')

    resposta2 = connexao2.recv(1024)
    if resposta2.decode() == '1':
        EnviarMensagem()
    elif resposta2.decode() == '2':
        Inscrição('2')
    elif resposta2.decode() == '3':
        Desinscrever('2')

    resposta3 = connexao3.recv(1024)
    if resposta1.decode() == '1':
        EnviarMensagem()
    elif resposta3.decode() == '2':
        Inscrição('3')
    elif resposta3.decode() == '3':
        Desinscrever('3')


#   Fecha as conexao do socket
connexao1.close()
connexao2.close()
connexao3.close()
