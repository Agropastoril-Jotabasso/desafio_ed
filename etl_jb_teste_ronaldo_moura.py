#Biblioteca de conexão com SGDB PostgresSQL
import psycopg2

# Informações para construção da string de conexão
host = "localhost"
dbname = "ETL"
user = "postgres"
password = "bi"
sslmode = "disable"

# Construção da string de conexão
conn_string = "host={0} user={1} dbname={2} password={3} sslmode={4}".format(host, user, dbname, password, sslmode)
conn = psycopg2.connect(conn_string)
print("Connexão estabelecida!")

#Abre cursor para execução de comandos
cursor = conn.cursor()

# Apaga tabela de Origem se existir
cursor.execute("DROP TABLE IF EXISTS BDGT;")
print("Tabela origem dropada com sucesso!")

# Cria tabela de Origem
cursor.execute("CREATE TABLE BDGT (AST VARCHAR (4) PRIMARY KEY, SEKT VARCHAR(10),JAHR VARCHAR(4),MONAT01 NUMERIC(18,3),MONAT02 NUMERIC(18,3),MONAT03 NUMERIC(18,3),MONAT04 NUMERIC(18,3),MONAT05 NUMERIC(18,3),MONAT06 NUMERIC(18,3),MONAT07 NUMERIC(18,3),MONAT08 NUMERIC(18,3),MONAT09 NUMERIC(18,3),MONAT10 NUMERIC(18,3),MONAT11 NUMERIC(18,3),MONAT12 NUMERIC(18,3))")
print("Tabela criada!")

# Apaga tabela de Destino se existir
cursor.execute("DROP TABLE IF EXISTS FATO_ORCAMENTO;")
print("Tabela destino dropada com sucesso!")

# Cria tabela de Destino
cursor.execute("CREATE TABLE FATO_ORCAMENTO (ID INTEGER PRIMARY KEY, FILIAL VARCHAR (4), SETOR VARCHAR(10),DT_ORCAMENTO DATE,VALOR NUMERIC(18,3))")
print("Tabela de destino criada!")

# Inserção de dados na tabela de Origem
cursor.execute("INSERT INTO BDGT (AST,SEKT,JAHR,MONAT01,MONAT02,MONAT03,MONAT04,MONAT05,MONAT06,MONAT07,MONAT08,MONAT09,MONAT10,MONAT11,MONAT12) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);",("0101","0000000001","2021",1256.23,1345.45,1120.00,1452.36,1356.65,1365.99,1001.23,1500.00,1860.00,1956.56,2000.21,2100.91))
cursor.execute("INSERT INTO BDGT (AST,SEKT,JAHR,MONAT01,MONAT02,MONAT03,MONAT04,MONAT05,MONAT06,MONAT07,MONAT08,MONAT09,MONAT10,MONAT11,MONAT12) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);",("0102","0000000001","2021",1256.23,1345.45,1120.00,1452.36,1356.65,1365.99,1001.23,1500.00,1860.00,1956.56,2000.21,2100.91))
cursor.execute("INSERT INTO BDGT (AST,SEKT,JAHR,MONAT01,MONAT02,MONAT03,MONAT04,MONAT05,MONAT06,MONAT07,MONAT08,MONAT09,MONAT10,MONAT11,MONAT12) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);",("0103","0000000001","2021",1256.23,1345.45,1120.00,1452.36,1356.65,1365.99,1001.23,1500.00,1860.00,1956.56,2000.21,2100.91))
print("Inserido 3 registros na tabela de origem - BDGT")

# Pega o ultimo id cadastrado no destino
cursor.execute("SELECT COALESCE(MAX(ID),0) FROM FATO_ORCAMENTO;")
rows = cursor.fetchall()
for row in rows:
	x = row[0]

# Utiliza função Fetch all para pegar retorno da execução da consulta a tabela de origem
cursor.execute("SELECT * FROM BDGT;")
rows = cursor.fetchall()

# Print todas as linhas retornadas
for row in rows:
	print("Registro Inserido BDGT = (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)" % (str(row[0]),str(row[1]),str(row[2]),str(row[3]),str(row[4]),str(row[5]),str(row[6]),str(row[7]),str(row[8]),str(row[9]),str(row[10]),str(row[11]),str(row[12]),str(row[13]),str(row[14])))
	# Inserção de dados na tabela destino
	for i in range(1,13):
		# Incrementa Id (chave da tabela destino)
		x = x + 1
		cursor.execute("INSERT INTO FATO_ORCAMENTO (ID,FILIAL,SETOR,DT_ORCAMENTO,VALOR) VALUES (%s,%s,%s,%s,%s);",(str(x),str(row[0]),str(row[1]),"1/"+str(i)+"/"+str(row[2]),str(row[i+2])))
		print ("Registro extraido e inserido = (%s,%s,%s,%s,%s) na FATO_ORCAMENTO" %(str(x),str(row[0]),str(row[1]),"1/"+str(i)+"/"+str(row[2]),str(row[i+2])))

print("Gerado %s registros na tabela FATO_ORCAMENTO derivados do ETL" % str(x))
	
# Libera recursos
conn.commit()
cursor.close()
conn.close()

print("Rotina finalizada!")

