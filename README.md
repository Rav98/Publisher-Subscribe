# Publisher-Subscribe

Este repositório contém uma implementação do método Publish-Subscribe, um metodo sobre comunicação em Sistemas Distribuídos, desenvolvido em Python. 

Este código foi desenvolvido para a apresentação de um minicurso da matéria COM242 - Sistemas Distribuídos do curso de Ciência da Computação da Universidade Federal de Itajubá - UNIFEI.

### Integrantes: 

Rafael Antunes Vieira - rafaelantunesvieira@unifei.edu.br - 2018000980

Flávio Mota Gomes - flavio.gomes@unifei.edu.br - 2018005379

Alef Aparecido de Paula Bispo - alef@unifei.edu.br - 2018008460

____________________________________________________________________________________________________

## Descrição dos arquivos:
###  servidor.py
O arquivo servidor.py contém as atribuições dos publishers e do broker. A aplicação utiliza de sockets para realizar o envio das mensagens e dados de comunicação entre publishers, broker e subscribers. Trata-se de uma implementação centralizada. Também é utilizada a biblioteca PyPubSub para gerenciar toda a lógica do sistema de Publish-Subscribe, fazendo o papel do broker na implementação.

###  cliente1.py, cliente2.py e cliente3.py
Os arquivos cliente1.py, cliente2.py e cliente3.py são iguais, a única coisa que difere entre os arquivos são as portas de conexão, sendo que cada porta se refere a um cliente diferente. Destaca-se que o cliente desta aplicação corresponde ao subcriber e que foram utilizados aqui três deles, mas que, devido à característica de escalabilidade do método, basta uma adaptação para inserção de quantos mais clientes forem necessários.

###  Pasta PersistenciaDados
Nesta pasta estão os arquivos de persistência de inscrições dos clientes. Nesta implementação, ocorre a persistência das inscrições e desinscrições realizadas pelos subscribers e o resultado dessas ações está dentro desta pasta, tendo cada um dos clientes um arquivo próprio. Por exemplo, o cliente1 tem seus dados persistidos em DadosCliente1.txt, e assim sucessivamente para os demais clientes.

## Executar a implementação:

1. Instale o Python 3 https://www.python.org/downloads/ 
2. Instale a biblioteca PyPubSub (https://pypi.org/project/PyPubSub/) com o comando: **"pip install PyPubSub"**
3. Abra o Terminal Linux ou o CMD do Windows e execute a aplicação do servidor: _Terminal Linux:_ **"python3 servidor.py"** ou _CMD Windows:_ **"servidor.py"**
4. Abra o Terminal Linux ou o CMD do Windows e execute a aplicação dos clientes: _Terminal Linux:_ **"python3 cliente1.py"** ou _CMD Windows:_ **"cliente1.py"**
5. Execute todos os clientes conforme a etapa 4

## Demonstração da aplicação:

Assista ao video de demostração da execução da aplicação por meio do seguinte link: https://youtu.be/NeskO--44fo

