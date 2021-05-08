#   Importando o socket
import socket

#   Importando a biblioteca do PyPubSub
from pubsub import pub

#   Definindo meu Host e porta
HOST = 'localhost'
PORT1 = 5001
PORT2 = 5002
PORT3 = 5003

# Publichers cadastrados
listaPub = ['Alef', 'Flavio', 'Rafael']

# Criando o objeto socket
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

#   Retorno do "aceitamento" da conexão
connexao1, endereco1 = pc1.accept()
print('Conectado com: ', endereco1)

connexao2, endereco2 = pc2.accept()
print('Conectado com: ', endereco2)

connexao3, endereco3 = pc3.accept()
print('Conectado com: ', endereco3)

# Envia a lista de Publishers:
for n in listaPub:
    connexao1.sendall(str.encode(n))
    connexao2.sendall(str.encode(n))
    connexao3.sendall(str.encode(n))

# Recebe Publisher escolhido pelos subscribes
listaRespSub1 = connexao1.recv(1024)
listaRespSub2 = connexao2.recv(1024)
listaRespSub3 = connexao3.recv(1024)

# imprime a escolha dos subscribes
print(listaRespSub1.decode())
print(listaRespSub2.decode())
print(listaRespSub3.decode())

#   Função que envia dados para o pc1

def pc1(data):
    connexao1.sendall(str.encode(data))


def pc2(data):
    connexao2.sendall(str.encode(data))


def pc3(data):
    connexao3.sendall(str.encode(data))


#   Função responsavel por inscrever os PCs nos grupos
pub.subscribe(pc1, listaRespSub1.decode())
pub.subscribe(pc2, listaRespSub2.decode())
pub.subscribe(pc3, listaRespSub3.decode())

#   Função responsavel por mandar as mensagens para determinado grupo inscrito
pub.sendMessage(listaRespSub1.decode(), data='SERVIDOR MANDOU PARA O PC1')
pub.sendMessage(listaRespSub2.decode(), data='SERVIDOR MANDOU PARA O PC2')
pub.sendMessage(listaRespSub3.decode(), data='SERVIDOR MANDOU PARA O PC3')

print('Mensagem enviada aos Clientes!')

#   Fecha as conexaos do socket
connexao1.close()
connexao2.close()
connexao3.close()
