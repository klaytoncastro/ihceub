# Exercícios

## Exercício 01: Criar uma simples aplicação Flask para registro de livros

### Objetivo: 

Crie uma aplicação Flask que permita ao usuário registrar um livro e listar todos os livros registrados. A aplicação não precisa usar um banco de dados: você pode armazenar os livros em uma lista. 

### Etapas:

- **Definir o modelo**:

1. Crie uma classe chamada Livro que tenha os atributos 'titulo' e 'autor'.

- **Criar rota para listar livros**:

2. Crie uma rota /livros que mostre todos os livros registrados.
Se não houver livros registrados, a página deve mostrar "Nenhum livro registrado."

- **Criar Rota para registrar um livro**:

3. Crie uma rota /adicionar que mostre um formulário permitindo ao usuário adicionar um novo livro (título e autor). Quando o formulário for submetido, o novo livro deve ser adicionado à lista de livros e o usuário deve ser redirecionado para a página /livros.

- **Criar rota para registrar um livro**:

4. Crie uma rota /adicionar que mostre um formulário permitindo ao usuário adicionar um novo livro (título e autor).
Quando o formulário for submetido, o novo livro deve ser adicionado à lista de livros e o usuário deve ser redirecionado para a página /livros. 