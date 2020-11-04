#Exemplo de conexão do Python com o SQL Server com autenticação do SQL Server, com necessidade de senha.
#Neste caso, pode ser utilizado quando a autentição for pelo SQL Server, pois, nota-se que possui a linha 15 ("pwd=SENHA") da maneira 1 e linha 36 da maneira 2.

#Nota: Não precisa ser executado com a função "def conectar()" a maneira 1, se quiser pode ser retirada. A maneira 2 necessita ser mantida.
#Nota2: Pode ser utilizado no Jupyter Notebook.
#Nota3: Por ser login no SQL Server com (Autenticação SQL Server), a linha de código 20 da maneira 1 e linha de código 40 da maneira 2 ("Trusted_Connection=no;") necessita estar como "no", indicando o login por esse tipo de autenticação SQL que requer senha.
#Nota4: Normalmente nas maneiras 1 e 2 , não temos como verificar realmente a mensagem de conexão, só vai ser possível com o teste de execução de uma query qualquer, pra isso criei as maneiras 3 e 4, para uma verificação realmente se temos conexão.

#Maneira 1 sem teste com query:
#Nota: Nesta maneira, não haverá nenhuma mensagem 

import pyodbc

def conectar():
    conexao = pyodbc.connect(
        "Driver={SQL Server Native Client 11.0};"
        "Server=SERVER;"
        "Database=DATABASENAME;"
        "uid=USUARIO;"
        "pwd=SENHA;"
        "Trusted_Connection=no;"
    )
conectar()

#----------#----------#----------#----------#----------#----------#----------#----------#----------#----------#----------#
#----------#----------#----------#----------#----------#----------#----------#----------#----------#----------#----------#
#----------#----------#----------#----------#----------#----------#----------#----------#----------#----------#----------#

#Maneira 2 sem teste com query:
#Nota: Nesta maneira, não haverá nenhuma mensagem 

import pyodbc

def conectar():
    try:
        conexao = pyodbc.connect(
            "Driver={SQL Server Native Client 11.0};"
            "Server=SERVER;"
            "Database=DATABASENAME;"
            "uid=USUARIO;"
            "pwd=SENHA;"
            "Trusted_Connection=no;"
        )
        return conexao.cursor()
    except:
        return 1

#----------#----------#----------#----------#----------#----------#----------#----------#----------#----------#----------#
#----------#----------#----------#----------#----------#----------#----------#----------#----------#----------#----------#
#----------#----------#----------#----------#----------#----------#----------#----------#----------#----------#----------#

#Maneira 3:
#Menção a maneira 1, mas, com teste de execução por uma query.

import pyodbc

def conectar():
    conexao = pyodbc.connect(
        "Driver={SQL Server Native Client 11.0};"
        "Server=SERVER;"
        "Database=DATABASENAME;"
        "uid=USUARIO;"
        "pwd=SENHA;"
        "Trusted_Connection=no;"
    )
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM ...")
    query_resultado = cursor.fetchall()
    print(query_resultado)

conectar()

#----------#----------#----------#----------#----------#----------#----------#----------#----------#----------#----------#
#----------#----------#----------#----------#----------#----------#----------#----------#----------#----------#----------#
#----------#----------#----------#----------#----------#----------#----------#----------#----------#----------#----------#

#Maneira 4:
#Menção a maneira 2, mas, com teste de execução por uma query.

import pyodbc

def conectar():
    try:
        conexao = pyodbc.connect(
            "Driver={SQL Server Native Client 11.0};"
            "Server=SERVER;"
            "Database=DATABASENAME;"
            "uid=USUARIO;"
            "pwd=SENHA;"
            "Trusted_Connection=no;"
        )
        return conexao.cursor()
    except:
        return 1

def query():
    try:
        cursor = conectar()
        cursor.execute("SELECT * FROM ...")
        query_resultado = cursor.fetchall()
    except:
        print('Não foi possivel retornar os dados da consulta.')
    finally:
        print(query_resultado)
        print('Consulta realizada com sucesso.')
query()