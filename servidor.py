#   Importando a biblioteca do Socket
from os import remove
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
listaPub = ['Futebol', 'Volei', 'Basquete']

global listaPubCalc
listaPubCalc = ['Diametro da Circunferencia',
                'Area da Circunferencia', 'Comprimento da Circunferencia']

# Classe cliente, contem a estrutura que cada cliente tera
class Cliente:
    def __init__(self, HOST, PORT):
        self.ListaInscricaoPub = []
        self.ListaInscricaoPubCalc = []
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((HOST, PORT))


#   Criando clientes
Cliente1 = Cliente(HOST, PORT1)
Cliente2 = Cliente(HOST, PORT2)
Cliente3 = Cliente(HOST, PORT3)


#   Colocando o socket em modo de escuta
print('\nSERVIDOR LIGADO!\n\nAguardando conexões......\n')
Cliente1.sock.listen()
Cliente2.sock.listen()
Cliente3.sock.listen()

#   Retorno da confirmação da conexão pelo Subscriber
connexao1, endereco1 = Cliente1.sock.accept()
print('Conectado com:', endereco1)

connexao2, endereco2 = Cliente2.sock.accept()
print('Conectado com:', endereco2)

connexao3, endereco3 = Cliente3.sock.accept()
print('Conectado com:', endereco3)


#   Função que envia dados para os Subscribers inscritos
def EnviaMensagemCliente1(data):
    connexao1.sendall(str.encode(data))


def EnviaMensagemCliente2(data):
    connexao2.sendall(str.encode(data))


def EnviaMensagemCliente3(data):
    connexao3.sendall(str.encode(data))


def PersistirDados(sub, Lista):
    #   Persistencia dos dados em arquivos
    if (sub == 1):
        arquivo1 = open("PersistenciaDados/DadosCliente1.txt", "w+")
        arquivo1.writelines(Lista)
        arquivo1.close()
    elif(sub == 2):
        arquivo2 = open("PersistenciaDados/DadosCliente2.txt", "w+")
        arquivo2.writelines(Lista)
        arquivo2.close()
    elif(sub == 3):
        arquivo3 = open("PersistenciaDados/DadosCliente3.txt", "w+")
        arquivo3.writelines(Lista)
        arquivo3.close()


# Função responsavel por inscrever o usuario em algum Publisher
def Inscrição(connexao, cliente, sub, lista):
    # Envia a lista de Publishers:
    for n in lista:
        connexao.sendall(str.encode(n))
    # Recebe Publisher escolhido pelo usuario
    MensagemRecebida = connexao.recv(1024)
    # Salva na lista o Publisher escolhido
    cliente.ListaInscricaoPub.append(MensagemRecebida.decode()+'\n')
    if(MensagemRecebida.decode() == 'Diametro da Circunferencia' or MensagemRecebida.decode() == 'Area da Circunferencia' or MensagemRecebida.decode() == 'Comprimento da Circunferencia'):
        cliente.ListaInscricaoPubCalc.append(MensagemRecebida.decode()+'\n')

    if(sub == 1):
        PersistirDados(1, cliente.ListaInscricaoPub)
        # imprime a escolha do usuario
        print('Subscriber ', sub, ' se inscreveu no:', MensagemRecebida.decode())
        #   Função responsavel por inscrever os Subscriber nos grupos
        pub.subscribe(EnviaMensagemCliente1, MensagemRecebida.decode()+'\n')
    elif(sub == 2):
        PersistirDados(2, cliente.ListaInscricaoPub)
        # imprime a escolha do usuario
        print('Subscriber ', sub, ' se inscreveu no:', MensagemRecebida.decode())
        #   Função responsavel por inscrever os Subscriber nos grupos
        pub.subscribe(EnviaMensagemCliente2, MensagemRecebida.decode()+'\n')
    elif(sub == 3):
        PersistirDados(3, cliente.ListaInscricaoPub)
        # imprime a escolha do usuario
        print('Subscriber ', sub, ' se inscreveu no:', MensagemRecebida.decode())
        #   Função responsavel por inscrever os Subscriber nos grupos
        pub.subscribe(EnviaMensagemCliente3, MensagemRecebida.decode()+'\n')


# Função responsavel por enviar a mensagem para cada Subscribers
def EnviarMensagem(opcao):
    #  Variavel contadora para contar as requisições de mensagem
    cont1 = 0
    cont2 = 0
    cont3 = 0
    #   Verifica se a mensagem é de texto ou é de numero para executar calculos
    #  1 para mensagens 2 para calculos
    if(opcao == 1):
        #  Laço para contar quantos Publishers o usuario esta inscrito
        for n in Cliente1.ListaInscricaoPub:
            if(n == 'Futebol'+'\n' or n == 'Volei'+'\n' or n == 'Basquete'+'\n'):
                cont1 = cont1+1
        #  Envia mensagem
        connexao1.sendall(str.encode(str(cont1)))
        for n in Cliente2.ListaInscricaoPub:
            if(n == 'Futebol'+'\n' or n == 'Volei'+'\n' or n == 'Basquete'+'\n'):
                cont2 = cont2+1
        connexao2.sendall(str.encode(str(cont2)))
        for n in Cliente3.ListaInscricaoPub:
            if(n == 'Futebol'+'\n' or n == 'Volei'+'\n' or n == 'Basquete'+'\n'):
                cont3 = cont3+1
        connexao3.sendall(str.encode(str(cont3)))
        # Recebe a mensagem e envia ao subscribers
        print('\nEscreva uma mensagem para os Subscribers do Publisher',
              listaPub[0], ':')
        data1 = input()
        pub.sendMessage(listaPub[0]+'\n', data=data1)

        print('\nEscreva uma mensagem para os Subscribers do Publisher',
              listaPub[1], ':')
        data2 = input()
        pub.sendMessage(listaPub[1]+'\n', data=data2)

        print('\nEscreva uma mensagem para os Subscribers do Publisher',
              listaPub[2], ':')
        data3 = input()
        pub.sendMessage(listaPub[2]+'\n', data=data3)
        print('\nMensagem enviada aos Subscribers!\n')

    elif(opcao == 2):
        #  Laço para contar quantos Publishers o usuario esta inscrito
        for n in Cliente1.ListaInscricaoPubCalc:
            cont1 = cont1+1
        #  Envia o numero de Publishers inscritos
        connexao1.sendall(str.encode(str(cont1)))
        for n in Cliente2.ListaInscricaoPubCalc:
            cont2 = cont2+1
        #  Envia o numero de Publishers inscritos
        connexao2.sendall(str.encode(str(cont2)))
        for n in Cliente3.ListaInscricaoPubCalc:
            cont3 = cont3+1
        #  Envia o numero de Publishers inscritos
        connexao3.sendall(str.encode(str(cont3)))
        #   Colhendo o numero do calculo
        print('\nEscreva um valor do raio para calculo ',
              listaPubCalc[0], ':')
        data1 = input()
        #   Envia o numero do calculo
        pub.sendMessage(listaPubCalc[0]+'\n', data=data1)
        #   Indica qual função utilizar
        pub.sendMessage(listaPubCalc[0]+'\n', data='1')

        print('\nEscreva um valor do raio para calculo ',
              listaPubCalc[1], ':')
        data2 = input()
        #   Envia o numero do calculo
        pub.sendMessage(listaPubCalc[1]+'\n', data=data2)
        #   Indica qual função utilizar
        pub.sendMessage(listaPubCalc[1]+'\n', data='2')

        print('\nEscreva um valor do raio para calculo ',
              listaPubCalc[2], ':')
        data3 = input()
        #   Envia o numero do calculo
        pub.sendMessage(listaPubCalc[2]+'\n', data=data3)
        #   Indica qual função utilizar
        pub.sendMessage(listaPubCalc[2]+'\n', data='3')

        print('\nMensagem enviada aos Subscribers!\n')


# Função responsavel por desinscrever o Subscriber
def Desinscrever(sub, cliente, connexao):
    # Envia a quantidade de Publishers o subscriber esta inscrito
    connexao.sendall(str.encode(str(len(cliente.ListaInscricaoPub))))
    # Envia a lista de Publishers o subscriber esta inscrito
    for n in cliente.ListaInscricaoPub:
        connexao.sendall(str.encode(n))
    # Recebe o dado com a informação de qual Pubisher o Subscribe quer se desinscrever
    RespMensagem = connexao.recv(1024)
    # Salva na lista
    cliente.ListaInscricaoPub.remove(RespMensagem.decode()+'\n')
    if(RespMensagem.decode() == 'Diametro da Circunferencia' or RespMensagem.decode() == 'Area da Circunferencia' or RespMensagem.decode() == 'Comprimento da Circunferencia'):
        cliente.listaPubCalc.remove(RespMensagem.decode()+'\n')
    if(sub == 1):
        PersistirDados(1, cliente.ListaInscricaoPub)
        # Chama a biblioteca PyPubSub para executar a desinscrição
        pub.unsubscribe(EnviaMensagemCliente1, RespMensagem.decode()+'\n')
        print('Subscriber ', sub, 'se desinscreveu do:',
              RespMensagem.decode())
    elif(sub == 2):
        PersistirDados(2, cliente.ListaInscricaoPub)
        # Chama a biblioteca PyPubSub para executar a desinscrição
        pub.unsubscribe(EnviaMensagemCliente2, RespMensagem.decode()+'\n')
        print('Subscriber ', sub, 'se desinscreveu do:',
              RespMensagem.decode())
    elif(sub == 3):
        PersistirDados(3, cliente.ListaInscricaoPub)
        # Chama a biblioteca PyPubSub para executar a desinscrição
        pub.unsubscribe(EnviaMensagemCliente3, RespMensagem.decode()+'\n')
        print('Subscriber ', sub, 'se desinscreveu do:',
              RespMensagem.decode())


#   Lendo o arquivo e aplicando os dados persistidos caso haja.
#   Restaurando os dados persistidos
arquivo1 = open("PersistenciaDados/DadosCliente1.txt", "r")
arquivo2 = open("PersistenciaDados/DadosCliente2.txt", "r")
arquivo3 = open("PersistenciaDados/DadosCliente3.txt", "r")

conteudo1 = arquivo1.readlines()
conteudo2 = arquivo2.readlines()
conteudo3 = arquivo3.readlines()

Cliente1.ListaInscricaoPub = conteudo1
Cliente2.ListaInscricaoPub = conteudo2
Cliente3.ListaInscricaoPub = conteudo3

for n1 in conteudo1:
    pub.subscribe(EnviaMensagemCliente1, n1)
    if(n1 == 'Diametro da Circunferencia'+'\n' or n1 == 'Area da Circunferencia'+'\n' or n1 == 'Comprimento da Circunferencia'+'\n'):
        Cliente1.ListaInscricaoPubCalc.append(n1)

for n2 in conteudo2:
    pub.subscribe(EnviaMensagemCliente2, n2)
    if(n2 == 'Diametro da Circunferencia'+'\n' or n2 == 'Area da Circunferencia'+'\n' or n2 == 'Comprimento da Circunferencia'+'\n'):
        Cliente2.ListaInscricaoPubCalc.append(n2)

for n3 in conteudo3:
    pub.subscribe(EnviaMensagemCliente3, n3)
    if(n3 == 'Diametro da Circunferencia'+'\n' or n3 == 'Area da Circunferencia'+'\n' or n3 == 'Comprimento da Circunferencia'+'\n'):
        Cliente3.ListaInscricaoPubCalc.append(n3)

arquivo1.close()
arquivo2.close()
arquivo3.close()

# Rotina de execução do servidor.
while True:
    # ouvindo os Subscribers para saber se eles querem se inscrever ou desinscrever
    resposta1 = connexao1.recv(1024)
    if resposta1.decode() == '1':
        EnviarMensagem(1)
    elif resposta1.decode() == '2':
        EnviarMensagem(2)
    elif resposta1.decode() == '3':
        Inscrição(connexao1, Cliente1, 1, listaPub)
    elif resposta1.decode() == '4':
        Inscrição(connexao1, Cliente1, 1, listaPubCalc)
    elif resposta1.decode() == '5':
        Desinscrever(1, Cliente1, connexao1)

    resposta2 = connexao2.recv(1024)
    if resposta2.decode() == '3':
        Inscrição(connexao2, Cliente2, 2, listaPub)
    elif resposta2.decode() == '4':
        Inscrição(connexao2, Cliente2, 2, listaPubCalc)
    elif resposta2.decode() == '5':
        Desinscrever(2, Cliente2, connexao2)

    resposta3 = connexao3.recv(1024)
    if resposta3.decode() == '3':
        Inscrição(connexao3, Cliente3, 3, listaPub)
    elif resposta3.decode() == '4':
        Inscrição(connexao3, Cliente3, 3, listaPubCalc)
    elif resposta3.decode() == '5':
        Desinscrever(3, Cliente3, connexao3)

#   Fecha as conexao do socket
connexao1.close()
connexao2.close()
connexao3.close()
