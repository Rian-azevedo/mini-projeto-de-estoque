🛒 Sistema de Estoque com Python (POO + SQLite)

Este projeto é um sistema simples de controle de estoque desenvolvido em Python, utilizando Programação Orientada a Objetos (POO) e banco de dados SQLite. Ideal para treinar conceitos de classes, modularização e persistência de dados.

---

📁 Estrutura do Projeto
estoque_app/
├── main.py # Código principal (interface via terminal)
├── banco.py # Conexão com o banco de dados e criação da tabela
└── classes/
    ├── init.py
    ├── estoque.py # Classe Estoque (operações com o banco)
    └── comandos.py # Classe Comandos (interação com o usuário)

---

🚀 Tecnologias usadas

- Python 3.13
- SQLite (módulo `sqlite3`)
- Programação Orientada a Objetos (POO)
- Terminal/CLI

---

⚙️ Funcionalidades

- [1] Cadastrar produtos
- [2] Listar produtos
- [3] Atualizar produtos por ID
- [4] Deletar produtos por ID

---

💡 Organização do código

- A classe `Estoque` está responsável pelas operações com o banco (salvar, mostrar, atualizar, deletar).
- A classe `Comandos` cuida apenas da **interação com o usuário** (inputs, prints), e chama os métodos da classe `Estoque` para realizar as ações.
- Isso separa bem a lógica do sistema (back-end) da interface (front-end de terminal).

---

## ▶️ Como rodar o projeto

1. Clone o repositório:
```bash
git clone https://github.com/Rian-azevedo/estoque_app.git
cd estoque_app
