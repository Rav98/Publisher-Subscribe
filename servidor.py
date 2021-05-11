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
global listaPub
listaPub = ['Futebol', 'Vôlei', 'Basquete']

#   Lista para salvar as inscrições de cada Subscriber
global ListaInscricaoPub1
ListaInscricaoPub1 = []
global listaInscricaoPub2
ListaInscricaoPub2 = []
global listaInscricaoPub3
ListaInscricaoPub3 = []

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
print('\nSERVIDOR LIGADO!\n\nAguardando conexões......\n')
sub1.listen()
sub2.listen()
sub3.listen()

#   Retorno da confirmação da conexão pelo Subscriber
connexao1, endereco1 = sub1.accept()
print('Conectado com:', endereco1)

connexao2, endereco2 = sub2.accept()
print('Conectado com:', endereco2)

connexao3, endereco3 = sub3.accept()
print('Conectado com:', endereco3)

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
        print('Subscriber 1 se inscreveu no:', RespSub1.decode())
        #   Função responsavel por inscrever os Subscriber nos grupos
        pub.subscribe(sub1, RespSub1.decode())
    elif(sub == '2'):
        # Envia a lista de Publishers:
        for n in listaPub:
            connexao2.sendall(str.encode(n))
        # Recebe Publisher escolhido pelo usuario
        RespSub2 = connexao2.recv(1024)
        ListaInscricaoPub2.append(RespSub2.decode())
        # imprime a escolha do usuario
        print('Subscriber 2 se inscreveu no:', RespSub2.decode())
        #   Função responsavel por inscrever os Subscribers nos grupos
        pub.subscribe(sub2, RespSub2.decode())
    elif(sub == '3'):
        # Envia a lista de Publishers:
        for n in listaPub:
            connexao3.sendall(str.encode(n))
        # Recebe Publisher escolhido pelo usuario
        RespSub3 = connexao3.recv(1024)
        ListaInscricaoPub3.append(RespSub3.decode())
        # imprime a escolha do usuario
        print('Subscriber 3 se inscreveu no:', RespSub3.decode())
        #   Função responsavel por inscrever os Subscribers nos grupos
        pub.subscribe(sub3, RespSub3.decode())


# Função responsavel por enviar a mensagem para cada Subscribers
def EnviarMensagem():
    #   Escolha da mensagem que se quer enviar
    print('\nEscreva uma mensagem para os Subscribers do Publisher',
          listaPub[0], ':')
    data1 = input()
    pub.sendMessage(listaPub[0], data=data1)
    print('\nEscreva uma mensagem para os Subscribers do Publisher',
          listaPub[1], ':')
    data2 = input()
    pub.sendMessage(listaPub[1], data=data2)
    print('\nEscreva uma mensagem para os Subscribers do Publisher',
          listaPub[2], ':')
    data3 = input()
    pub.sendMessage(listaPub[2], data=data3)
    print('\nMensagem enviada aos Subscribers!\n')


# Função responsavel por desinscrever o Subscriber
def Desinscrever(sub):
    if (sub == '1'):
        # Envia a quantidade de Publishers o subscriber esta inscrito
        connexao1.sendall(str.encode(str(len(ListaInscricaoPub1))))
        # Envia a lista de Publishers o subscriber esta inscrito
        for n in ListaInscricaoPub1:
            connexao1.sendall(str.encode(n))
        # Recebe o dado com a informação de qual Pubisher o Subscribe quer se desinscrever
        RespSub1 = connexao1.recv(1024)
        # Salva na lista
        ListaInscricaoPub1.remove(RespSub1.decode())
        # Chama a biblioteca PyPubSub para executar a desinscrição
        pub.unsubscribe(sub1, RespSub1.decode())
        print('Subscriber1 se desinscreveu do:', RespSub1.decode())
    elif (sub == '2'):
        # Envia a quantidade de Publishers o subscriber esta inscrito
        connexao2.sendall(str.encode(str(len(ListaInscricaoPub2))))
        # Envia a lista de Publishers o subscriber esta inscrito
        for n in ListaInscricaoPub2:
            connexao2.sendall(str.encode(n))
        # Recebe o dado com a informação de qual Pubisher o Subscribe quer se desinscrever
        RespSub2 = connexao2.recv(1024)
        # Salva na lista
        ListaInscricaoPub2.remove(RespSub2.decode())
        # Chama a biblioteca PyPubSub para executar a desinscrição
        pub.unsubscribe(sub2, RespSub2.decode())
        print('Subscriber2 se desinscreveu do:', RespSub2.decode())
    elif (sub == '3'):
        # Envia a quantidade de Publishers o subscriber esta inscrito
        connexao3.sendall(str.encode(str(len(ListaInscricaoPub3))))
        # Envia a lista de Publishers o subscriber esta inscrito
        for n in ListaInscricaoPub3:
            connexao3.sendall(str.encode(n))
        # Recebe o dado com a informação de qual Pubisher o Subscribe quer se desinscrever
        RespSub3 = connexao3.recv(1024)
        # Salva na lista
        ListaInscricaoPub3.remove(RespSub3.decode())
        # Chama a biblioteca PyPubSub para executar a desinscrição
        pub.unsubscribe(sub3, RespSub3.decode())
        print('Subscriber3 se desinscreveu do:', RespSub3.decode())


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
    if resposta2.decode() == '2':
        Inscrição('2')
    elif resposta2.decode() == '3':
        Desinscrever('2')

    resposta3 = connexao3.recv(1024)
    if resposta3.decode() == '2':
        Inscrição('3')
    elif resposta3.decode() == '3':
        Desinscrever('3')


#   Fecha as conexao do socket
connexao1.close()
connexao2.close()
connexao3.close()
