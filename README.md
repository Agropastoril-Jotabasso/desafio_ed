## Desafio - Engenheiro(a) de Dados Jotabasso
**Contexto:**
Precisa ser criada uma rotina de ETL para os dados de orçamento da empresa para utilizá-los em um dashboard. Abaixo temos a tabela de origem e o dicionário de dados dela:

![Modelagem Tabela de Oridem](https://i.imgur.com/e1V5IJu.png)

* AST: Filial que foi feito o orçamento
* SEKT: Código de Setor
* JAHR: Ano do orçamento
* MONAT01: Valor do Orçamento referente ao mês de Janeiro
* MONAT02: Valor do Orçamento referente ao mês de Fevereiro
* MONAT03: Valor do Orçamento referente ao mês de Março
* MONAT04: Valor do Orçamento referente ao mês de Abril
* MONAT05: Valor do Orçamento referente ao mês de Maio
* MONAT06: Valor do Orçamento referente ao mês de Junho
* MONAT07: Valor do Orçamento referente ao mês de Julho
* MONAT08: Valor do Orçamento referente ao mês de Agosto
* MONAT09: Valor do Orçamento referente ao mês de Setembro
* MONAT10: Valor do Orçamento referente ao mês de Outubro
* MONAT11: Valor do Orçamento referente ao mês de Novembro
* MONAT12: Valor do Orçamento referente ao mês de Dezembro

Já no destino, é preciso ter os valores por data na linha. Estrutura e dicionário de dados:

![Modelagem Tabela de Destino](https://i.imgur.com/sz7oEJ1.png)

* FILIAL: Filial que o orçamento foi feito
* SETOR: Código de Setor
* DT_ORCAMENTO: Data do orçamento (utilizar primeiro dia do mês)
* VALOR: Valor do Orçamento

**Resultados esperados:**

 1. Criação das tabelas BDGT e FATO_ORCAMENTO (pode ser no mesmo banco de dados);
 2. Criação script em Python para realizar o ETL;
 3. Documentação do projeto em markdown no GitHub;
 4. Disponibilizar todo o código fonte em uma *Fork* neste repositório;

**Tecnologias obrigatórias:**

 1. Linguagem Python;
 2. Banco de Dados PostgreSQL;
 3. Versionamento de código no GitHub;

**Opcionais (não obrigatórios):**

 1. Deploy do projeto na AWS
 2. Utilizar GitHub Action (CI/CD) para deploy

Prazo de entrega é de 15 dias.

Boa sorte!

**Att**
**Time de Business Intelligence**
