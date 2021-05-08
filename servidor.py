#   Importando o socket
import socket

#   Importando a biblioteca do PyPubSub
from pubsub import pub

#   Definindo meu Host e porta
HOST = 'localhost'
PORT1 = 5001
PORT2 = 5002
PORT3 = 5003

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
print('Conectado em: ', endereco1)

connexao2, endereco2 = pc2.accept()
print('Conectado em: ', endereco2)

connexao3, endereco3 = pc3.accept()
print('Conectado em: ', endereco3)

#   Conecao feita, hora de configura o PubSub ----------------

#   Função que envia dados para o pc1
def pc1(data):
    connexao1.sendall(str.encode(data))

#   Função que envia dados para o pc2
def pc2(data):
    connexao2.sendall(str.encode(data))

#   Função que envia dados para o pc2
def pc3(data):
    connexao3.sendall(str.encode(data))

#   Função responsavel por inscrever os PCs nos grupos 
pub.subscribe(pc1, 'Rafael')
pub.subscribe(pc2, 'Flavio')
pub.subscribe(pc3, 'Alef')

#   Função responsavel por mandar as mensagens para determinado grupo inscrito
pub.sendMessage('Rafael', data='SERVIDOR MANDOU PARA O PC1')
pub.sendMessage('Flavio', data='SERVIDOR MANDOU PARA O PC2')
pub.sendMessage('Alef', data='SERVIDOR MANDOU PARA O PC3')  

print('Mensagem enviada aos Clientes!')

#   Fecha as conexaos do socket
connexao1.close()
connexao2.close()
connexao3.close()