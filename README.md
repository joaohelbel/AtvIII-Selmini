
# 🛒 Plataforma Concorrente de Processamento de Pedidos

Projeto desenvolvido como parte da disciplina **Programação III** – ESPM  
📚 Prof. Dr. Antonio Marcos Selmini – [antonio.selmini@espm.br](mailto:antonio.selmini@espm.br)  

###

## 👥 Alunos

- **Henrique Lecce** ([hqlcc](https://github.com/hqlcc))
- **João Pedro Helbel** ([joaohelbel](https://github.com/joaohelbel))

Repositório: [github.com/joaohelbel/AtvIII-Selmini](https://github.com/joaohelbel/AtvIII-Selmini)

###

## 📝 Descrição

Este projeto simula uma aplicação web para processamento concorrente e transacional de pedidos em uma loja virtual. Os pedidos são processados em paralelo com controle de transações para garantir a **consistência e integridade** dos dados, mesmo em cenários com múltiplos acessos simultâneos.

###

## ✅ Funcionalidades

- Cadastro inicial de **clientes** (nome, saldo) e **produtos** (nome, preço, estoque)
- Processamento de **pedidos concorrentes**, com:
  - Validação de saldo e estoque
  - Transação atômica: rollback automático em caso de erro
  - Atualização consistente do banco de dados
- API RESTful via Flask:
  - `POST /pedido` – Simula a chegada de um novo pedido
  - `GET /relatorio` – Lista os pedidos processados com sucesso
  - `GET /status` *(opcional)* – Exibe estatísticas de pedidos

###

## 🛠️ Tecnologias Utilizadas

| Tecnologia            | Uso                           |
|------------------------|-------------------------------|
| Python 3.x             | Lógica da aplicação           |
| Flask                  | API Web                       |
| SQLAlchemy + MySQL     | ORM + Banco relacional        |
| ThreadPoolExecutor     | Concorrência real             |
| `mysql-connector-python` | Driver de conexão MySQL     |

###

## ⚙️ Como Executar

### 1. Clone o repositório

```
git clone https://github.com/joaohelbel/AtvIII-Selmini.git
cd AtvIII-Selmini
```

### 2. Crie um ambiente virtual

```
python -m venv venv
venv\Scripts\activate   # Windows
# ou
source venv/bin/activate  # Linux/macOS
```

### 3. Instale as dependências

```
pip install -r requirements.txt
```

###

### 4. Crie o banco de dados no MySQL

Abra seu MySQL local e execute:

```sql
CREATE DATABASE eletromercio;
```

⚠️ **Importante**: certifique-se de que o usuário `root` tem senha `root`.  
Caso contrário, altere o arquivo `config.py`:

```python
conexao_banco = 'mysql+mysqlconnector://root:root@localhost/eletromercio'
```

###

### 5. Crie as tabelas do projeto

```
python criar_tabela.py
```

###

### 6. Popule o banco com clientes e produtos

```
python popularBanco.py
```

###

### 7. Inicie o servidor Flask

```
python app.py
```

Abra o navegador:

- 🏠 Home: http://127.0.0.1:5000
- 📋 Relatório: http://127.0.0.1:5000/relatorio
- 📊 Status: http://127.0.0.1:5000/status

###

### 8. Teste de concorrência (20 pedidos simultâneos)

Em outro terminal, execute:

```
python testes_pedidos.py
```

O sistema processará múltiplos pedidos simultaneamente, utilizando `ThreadPoolExecutor` e garantindo **transações atômicas** (com rollback em falhas).

###

