**Projeto: Sistema de Gestão de Biblioteca em Python**

### Classes Principais:

1. **Livro:**
   - **Atributos:**
     - Título
     - Autor
     - Ano de Publicação
     - Disponibilidade (indicando se o livro está emprestado ou não).
   - **Métodos:**
     - `emprestar()`: Atualiza o estado de disponibilidade para emprestado.
     - `devolver()`: Atualiza o estado de disponibilidade para disponível.

2. **Usuário:**
   - **Atributos:**
     - Nome
     - ID do Usuário.
   - **Métodos:**
     - `pegar_emprestado(livro)`: Adiciona um livro à lista de livros emprestados pelo usuário.
     - `devolver(livro)`: Remove um livro da lista de livros emprestados pelo usuário.

3. **Biblioteca:**
   - **Atributos:**
     - Lista de Livros
     - Lista de Usuários.
   - **Métodos:**
     - `adicionar_livro(livro)`: Adiciona um livro à biblioteca.
     - `remover_livro(livro)`: Remove um livro da biblioteca.
     - `cadastrar_usuario(usuario)`: Adiciona um usuário à biblioteca.
     - `remover_usuario(usuario)`: Remove um usuário da biblioteca.
     - `listar_livros_disponiveis()`: Apresenta a lista de livros disponíveis.
     - `listar_livros_emprestados()`: Apresenta a lista de livros atualmente emprestados.

### Fluxo do Programa:

1. Criação de objetos `Livro` e `Usuário`.
2. Adição desses objetos à `Biblioteca`.
3. Usuários podem pegar emprestado e devolver livros através dos métodos da `Biblioteca`.
4. Exibição de informações sobre livros disponíveis e emprestados.

### Objetivos do Projeto:

1. **Prática de POO:**
   - Implementação de encapsulamento, herança e polimorfismo.
   - Uso de métodos especiais como `__init__`, `__str__` (para representação de string), etc.

2. **Gestão de Estado:**
   - Manipulação eficiente do estado de disponibilidade dos livros.
   - Registro de livros emprestados por usuários.

3. **Interação com Usuários:**
   - Permitir que usuários interajam com o sistema, pegando emprestado e devolvendo livros.

4. **Organização da Biblioteca:**
   - Métodos para adicionar e remover livros e usuários, mantendo a biblioteca organizada.

### Possíveis Extensões do Projeto:

1. **Histórico de Empréstimos:**
   - Manter um histórico de empréstimos, incluindo datas.

2. **Validações Adicionais:**
   - Implementar verificações de validade ao adicionar ou remover livros/usuários.

3. **Pesquisa e Classificação:**
   - Adicionar métodos para pesquisar livros por autor, título, etc.
   - Implementar classificação de livros por gênero ou outros critérios.

4. **Interface Gráfica ou Web:**
   - Estender o projeto para ter uma interface gráfica ou web para interação.

Este projeto proporcionará uma prática sólida de conceitos de POO, organização de código e manipulação de estados em Python.
