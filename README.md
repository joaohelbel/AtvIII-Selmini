
# 💻 Plataforma Concorrente de Processamento de Pedidos

Projeto desenvolvido como atividade da disciplina **Programação III** – ESPM  
Prof. Dr. Antonio Marcos Selmini – [antonio.selmini@espm.br](mailto:antonio.selmini@espm.br)  
📅 Entrega: até 23/05/2025 às 23h59

---

## 👥 Alunos

- **Henrique Lecce** ([hqlcc](https://github.com/hqlcc))
- **João Pedro Helbel** ([joaohelbel](https://github.com/joaohelbel))

---

## 📝 Descrição

Esta aplicação simula o ambiente de uma startup de comércio eletrônico que precisa processar múltiplos pedidos de compra de maneira **concorrente, segura e escalável**, utilizando:

- Concorrência com `ThreadPoolExecutor`
- Transações atômicas com `SQLAlchemy`
- API RESTful com `Flask`
- Banco de dados relacional (`MySQL`)

---

## 🎯 Funcionalidades

- ✅ Cadastro de **clientes** com nome e saldo
- ✅ Cadastro de **produtos** com nome, preço e estoque
- ✅ Processamento de **pedidos concorrentes**, garantindo:
  - Validação de saldo e estoque
  - Criação do pedido e itens
  - Atualização atômica do banco
  - Rollback automático em caso de erro
- ✅ API RESTful:
  - `POST /pedido` – Simula a chegada de um novo pedido (executado em paralelo)
  - `GET /relatorio` – Lista os pedidos concluídos com sucesso
  - `GET /status` *(opcional)* – Exibe estatísticas de pedidos em andamento ou finalizados

---

## 🛠️ Tecnologias Utilizadas

| Tecnologia     | Uso                          |
|----------------|------------------------------|
| Python 3.x     | Lógica da aplicação          |
| Flask          | API Web                      |
| SQLAlchemy     | ORM e transações             |
| MySQL          | Banco de dados relacional    |
| ThreadPoolExecutor | Execução concorrente     |

---
