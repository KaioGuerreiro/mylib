# 📚 MyLib

MyLib é uma aplicação web onde usuários podem cadastrar seus livros, acompanhar o progresso de leitura e atribuir notas. O projeto é dividido em backend (Django REST Framework) e frontend (React), com autenticação de usuários e consumo de API.

---

## ⚙️ Tecnologias utilizadas

### Backend

- Python 3.13
- Django
- Django REST Framework
- pipenv (gerenciador de ambiente)
- Autenticação Token

### Frontend

- React
- Vite
- React Router

---

## 🚀 Funcionalidades

- Cadastro e login de usuários
- Cadastro de livros com título, autor, nota e total de páginas
- Registro do progresso de leitura
- Listagem dos livros e status de leitura por usuário
- Backend com API REST protegida por token de autenticação

---

## 🛠️ Instalação

### Backend

```bash
# Clone o repositório e acesse a pasta do backend
git clone https://github.com/KaioGuerreiro/mylib.git
cd mylib/backend

# Instale o pipenv se ainda não tiver
pip install pipenv

# Crie o ambiente virtual e instale as dependências
pipenv install
pipenv shell

# Execute as migrações
cd mylib
python manage.py migrate

# Inicie o servidor
python manage.py runserver
```

### Frontend

```bash

# Acesse a pasta do frontend
cd ../frontend

# Instale as dependências
npm install

# Inicie a aplicação
npm run dev
```

---

### 💡 Objetivo

Este projeto foi desenvolvido como parte do meu portfólio pessoal, com o objetivo de praticar conceitos de backend com Django e frontend com React, além da integração entre as tecnologias com autenticação.

Documentaçao: [Notion](https://www.notion.so/MyLib-Doc-1f01a8bc25c7804cb844d51eeb666894?pvs=4)

---

### 📬 Contato

Feito com ❤️ por Kaio Rodrigo
[LinkedIn](https://www.linkedin.com/in/kaioguerreiro/) • [GitHub](https://github.com/KaioGuerreiro)
