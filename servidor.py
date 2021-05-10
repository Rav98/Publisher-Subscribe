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
listaPub = ['Alef', 'Flavio', 'Rafael']

#   Lista para salvar as inscrições de cada Subscribe
global listaDeinscricaoPC1
listaDeinscricaoPC1 = []
global listaDeinscricaoPC2
listaDeinscricaoPC2 = []
global listaDeinscricaoPC3
listaDeinscricaoPC3 = []

#   Variaveis globais para salvar as respostas retornadas pelos Subscribers
global listaRespSub1
global listaRespSub2
global listaRespSub3

#   Criando o objeto socket para cada inscrito
pc1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
pc2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
pc3 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#   Vincular servidor e porta oa socket
pc1.bind((HOST, PORT1))
pc2.bind((HOST, PORT2))
pc3.bind((HOST, PORT3))

#   Colocando o socket em modo de escuta
pc1.listen()
print('Aguardando conexao do PC1')

pc2.listen()
print('Aguardando conexao do PC2')

pc3.listen()
print('Aguardando conexao do PC3')

#   Retorno da confirmação da conexão pelo Subscribe
connexao1, endereco1 = pc1.accept()
print('Conectado com: ', endereco1)

connexao2, endereco2 = pc2.accept()
print('Conectado com: ', endereco2)

connexao3, endereco3 = pc3.accept()
print('Conectado com: ', endereco3)

#   Função que envia dados para os Subscribers inscritos


def pc1(data):
    connexao1.sendall(str.encode(data))


def pc2(data):
    connexao2.sendall(str.encode(data))


def pc3(data):
    connexao3.sendall(str.encode(data))


# Função responsavel por inscrever o usuario em algum Publisher
def Inscrição(pc):
    if(pc == '1'):
        # Envia a lista de Publishers:
        for n in listaPub:
            connexao1.sendall(str.encode(n))
        # Recebe Publisher escolhido pelo usuario
        listaRespSub1 = connexao1.recv(1024)
        listaDeinscricaoPC1.append(listaRespSub1.decode())
        # imprime a escolha do usuario
        print('PC1 escolheu se inscrever em:', listaRespSub1.decode())
        #   Função responsavel por inscrever os Subscribe nos grupos
        pub.subscribe(pc1, listaRespSub1.decode())

    elif(pc == '2'):
        # Envia a lista de Publishers:
        for n in listaPub:
            connexao2.sendall(str.encode(n))
        # Recebe Publisher escolhido pelo usuario
        listaRespSub2 = connexao2.recv(1024)
        listaDeinscricaoPC2.append(listaRespSub2.decode())
        # imprime a escolha do usuario
        print('PC2 escolheu se inscrever em:', listaRespSub2.decode())
        #   Função responsavel por inscrever os Subscribe nos grupos
        pub.subscribe(pc2, listaRespSub2.decode())

    elif(pc == '3'):
        # Envia a lista de Publishers:
        for n in listaPub:
            connexao3.sendall(str.encode(n))
        # Recebe Publisher escolhido pelo usuario
        listaRespSub3 = connexao3.recv(1024)
        listaDeinscricaoPC3.append(listaRespSub3.decode())
        # imprime a escolha do usuario
        print('PC3 escolheu se inscrever em:', listaRespSub3.decode())
        #   Função responsavel por inscrever os Subscribe nos grupos
        pub.subscribe(pc3, listaRespSub3.decode())

# Função responsavel por enviar a mensagem para cada Subscribe


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

# Função responsavel por desinscrever o Subscribe


def Desinscrever(pc):
    if (pc == '1'):
        connexao1.sendall(str.encode(str(len(listaDeinscricaoPC1))))
        for n in listaDeinscricaoPC1:
            connexao1.sendall(str.encode(n))
        listaRespSub1 = connexao1.recv(1024)
        listaDeinscricaoPC1.remove(listaRespSub1.decode())
        pub.unsubscribe(pc1, listaRespSub1.decode())
        print('PC1 se desinscreveu de:', listaRespSub1.decode())
    elif (pc == '2'):
        connexao2.sendall(str.encode(str(len(listaDeinscricaoPC2))))
        for n in listaDeinscricaoPC2:
            connexao2.sendall(str.encode(n))
        listaRespSub2 = connexao2.recv(1024)
        listaDeinscricaoPC2.remove(listaRespSub2.decode())
        pub.unsubscribe(pc2, listaRespSub2.decode())
        print('PC2 se desinscreveu de:', listaRespSub2.decode())
    elif (pc == '3'):
        connexao3.sendall(str.encode(str(len(listaDeinscricaoPC3))))
        for n in listaDeinscricaoPC3:
            connexao3.sendall(str.encode(n))
        listaRespSub3 = connexao3.recv(1024)
        listaDeinscricaoPC3.remove(listaRespSub3.decode())
        pub.unsubscribe(pc3, listaRespSub3.decode())
        print('PC3 se desinscreveu de:', listaRespSub3.decode())


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


#   Fecha as conexaos do socket
connexao1.close()
connexao2.close()
connexao3.close()
