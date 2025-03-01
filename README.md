# Users API

## Descrição

Esta é uma API para gerenciar usuários, construída com Flask e SQLAlchemy.

## Pré-requisitos

- Docker
- Python 3.10+
- PostgreSQL

## Configuração

### 1. Configurar variáveis de ambiente

Certifique-se de ter configurado o arquivo `.env` na raiz do projeto baseado no arquivo `.env.example`, com as variáveis de ambiente necessárias para execução do projeto.

### 2. Rodar o Docker Compose

Execute o comando abaixo para iniciar o contêiner do PostgreSQL:

```sh
docker compose up -d
```

### 3. Crie as tabelas

```sh
python3 create-tables.py
```

### Como executar

Para executar o projeto em modo de desenvolvimento.

```bash
python3 app.py
```
