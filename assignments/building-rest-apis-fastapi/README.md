# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Construa uma API REST para gerenciar livros usando FastAPI, modelos Pydantic e métodos HTTP. Pratique rotas, validação de dados, códigos de status e respostas de erro.

## 📝 Tasks

### 🛠️ Criar a rota para listar livros

#### Descrição

Complete o código inicial para executar uma aplicação FastAPI e disponibilizar a coleção de livros por uma rota HTTP.

#### Requisitos

O programa concluído deve:

- Instalar as dependências com `python -m pip install fastapi uvicorn`.
- Criar uma aplicação FastAPI executável com `uvicorn starter-code:app --reload`.
- Implementar `GET /books` para retornar todos os livros como JSON com status `200`.
- Permitir que a documentação interativa da API seja acessada em `/docs`.

### 🛠️ Criar livros com validação

#### Descrição

Implemente a rota para adicionar um livro à coleção. Use o modelo Pydantic fornecido para validar os dados recebidos no corpo da requisição.

#### Requisitos

O programa concluído deve:

- Implementar `POST /books` com os campos `title`, `author` e `year`.
- Gerar um identificador para cada novo livro e adicioná-lo à coleção.
- Retornar o livro criado, incluindo seu identificador, com status `201`.
- Rejeitar requisições com campos ausentes ou tipos incompatíveis por meio da validação do FastAPI.

Exemplo de corpo da requisição:

```json
{
  "title": "Kindred",
  "author": "Octavia E. Butler",
  "year": 1979
}
```

### 🛠️ Consultar um livro por identificador

#### Descrição

Crie uma rota para localizar um livro específico pelo seu identificador e responder adequadamente quando ele não existir.

#### Requisitos

O programa concluído deve:

- Implementar `GET /books/{book_id}`.
- Retornar os dados do livro com status `200` quando o identificador existir.
- Retornar status `404` com uma mensagem de erro quando o livro não for encontrado.

### 🛠️ Atualizar e remover livros

#### Descrição

Complete as operações de atualização e remoção para que os clientes possam gerenciar os livros existentes.

#### Requisitos

O programa concluído deve:

- Implementar `PUT /books/{book_id}` para substituir os campos do livro usando o modelo Pydantic.
- Retornar o livro atualizado com status `200` ou status `404` se o identificador não existir.
- Implementar `DELETE /books/{book_id}` para remover um livro existente e responder com status `204`.
- Retornar status `404` ao tentar remover um livro inexistente.