# Sistema de Login em Python

Este é um sistema de login básico desenvolvido em Python usando `CustomTkinter` para a interface gráfica e `sqlite3` para gerenciamento de usuários.

## Funcionalidades
- Registro de novos usuários com nome de usuário e senha.
- Login de usuários com verificação de credenciais.
- Senhas encriptadas usando `bcrypt`.

## Estrutura do Projeto
- `src/main.py`: Código principal do sistema de login.
- `database/usuarios.db`: Banco de dados SQLite para armazenar usuários.

## Instalação e Execução
1. Clone o repositório:
    ```bash
    git clone https://github.com/paulocastanha33/login_python_sqlite.git
    ```

2. Navegue até a pasta do projeto:
    ```bash
    cd login_system
    ```

3. Instale as dependências:
    ```bash
    pip install customtkinter bcrypt
    ```

4. Execute o programa:
    ```bash
    python src/main.py
    ```

## Criação do Executável
Para criar um executável do programa, utilize `PyInstaller`:
```bash
pip install pyinstaller
pyinstaller --onefile app.py
