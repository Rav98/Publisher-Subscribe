# Publisher-Subscribe

Este repositório contem uma implementação do método Publish-Subscribe, um metodo sobre comunicação em Sistemas Distribuídos desenvolvido em Python. 

Este código foi desenvolvido para a apresentação de um Mini-Curso da matéria COM242 - Sistemas Distribuídos do curso de Ciência da Computação da Universidade Federal de Itajubá - UNIFEI.

### Integrantes: 

Rafael Antunes Vieira - rafaelantunesvieira@unifei.edu.br - 2018000980

Flávio Mota Gomes - flavio.gomes@unifei.edu.br - 2018005379

Alef Aparecido de Paula Bispo - alef@unifei.edu.br - 2018008460

____________________________________________________________________________________________________

## Descrição dos arquivos:
###  servidor.py
O arquivo servidor.py contém as atribuições dos Publishers e do Broker. A aplicação utiliza de sockets para realizar o envio das mensagens e dados de comunicação entre Publishers, Broker e Subscribers. Também é utilizada a biblioteca PyPubSub para gerenciar toda a lógica do sistema de Publishe-Subscribe, fazendo o papel do broker na implementação.

###  cliente1.py, cliente2.py e cliente3.py
Os arquivos cliente1.py, cliente2.py e cliente3.py são iguais, a unica coisa que difere entre os arquivos são as portas de conexão, cada porta refere-se a um cliente diferente. Destaca-se, que o cliente desta aplicação corresponde ao subcriber e que utilizou-se aqui três, mas que basta uma adaptação para inserção de quantos mais forem necessários.

###  Pasta PersistenciaDados
Os arquivos nesta pasta, são os arquivos de percistencia dos Publishers de cada cliente, isto é, nesta implementação é feita a percistencia das inscrições e desiscrições de cada cliente e é salvo nos arquivos que estão nesta pasta. O arquivo DadosCliente1.txt corresponde aos Publishers que o cliente1 esta inscrito. Segue a mesma logica para os outros arquivos: DadosCliente2.txt e DadosCliente3.txt.

## Executar a implementação:

1. Instale o Python 3 https://www.python.org/downloads/ 
2. instale a biblioteca PyPubSub (https://pypi.org/project/PyPubSub/) com o comando: **"pip install PyPubSub"**
3. Abra o Terminal Linux ou o CMD do Windows e execute a aplicação do servidor: _Terminal Linux:_ **"python3 servidor.py"** ou _CMD Windows:_ **"servidor.py"**
4. Abra o Terminal Linux ou o CMD do Windows e execute a aplicação dos clientes: _Terminal Linux:_ **"python3 cliente1.py"** ou _CMD Windows:_ **"cliente1.py"**
5. Execute todos os clientes conforme a etapa 4

## Demonstração da aplicação:

Assista o video de demostração da execução da aplicação: https://youtu.be/NeskO--44fo

