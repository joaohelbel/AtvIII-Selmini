
# 🛒 Plataforma Concorrente de Processamento de Pedidos

Projeto desenvolvido como parte da disciplina **Programação III** – ESPM  
📚 Prof. Dr. Antonio Marcos Selmini – [antonio.selmini@espm.br](mailto:antonio.selmini@espm.br)  

---

## 👥 Alunos

- **Henrique Lecce** ([hqlcc](https://github.com/hqlcc))
- **João Pedro Helbel** ([joaohelbel](https://github.com/joaohelbel))

Repositório: [github.com/joaohelbel/AtvIII-Selmini](https://github.com/joaohelbel/AtvIII-Selmini)

---

## 📝 Descrição

Este projeto simula uma aplicação web para processamento concorrente e transacional de pedidos em uma loja virtual. Os pedidos são processados em paralelo com controle de transações para garantir a **consistência e integridade** dos dados, mesmo em cenários com múltiplos acessos simultâneos.

---

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

---

## 🛠️ Tecnologias Utilizadas

| Tecnologia            | Uso                           |
|------------------------|-------------------------------|
| Python 3.x             | Lógica da aplicação           |
| Flask                  | API Web                       |
| SQLAlchemy + MySQL     | ORM + Banco relacional        |
| ThreadPoolExecutor     | Concorrência real             |
| `mysql-connector-python` | Driver de conexão MySQL     |

---

## 🌐 Configuração da API

- **Host**: `0.0.0.0`  
- **Porta**: `3000`  
- **Banco de dados**:  
  `mysql+mysqlconnector://root:root@localhost/comercio_eletrônico`  
- **Fonte de dados externa (simulação)**:  
  `https://iagen.espm.br/sensores/dados`

---

## ⚙️ Como Executar

### 1. Clone o repositório

```bash
git clone https://github.com/joaohelbel/AtvIII-Selmini.git
cd AtvIII-Selmini
```

### 2. Crie um ambiente virtual

```
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

### 3. Instale as dependências
```
pip install -r requirements.txt
```

### 4. Configure e crie o banco de dados
```
CREATE DATABASE comercio_eletrônico;
```

#### Depois, execute o script de criação/povoamento:
```
python setup_db.py
```

### 5. Inicie o servidor Flask
```
python app.py
```
