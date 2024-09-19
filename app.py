import sqlite3
import customtkinter as ctk
import bcrypt  # Biblioteca para encriptografar senha
from tkinter import messagebox

# Configurando a interface gráfica
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

# Conectando ao banco de dados
conn = sqlite3.connect("usuarios.db")
cursor = conn.cursor()

# Criar tabela caso não exista
cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT UNIQUE NOT NULL,
                    password TEXT NOT NULL)''')
conn.commit()

# Função para registrar usuário
def registrar_usuario():
    username = entry_username.get()
    password = entry_password.get()

    if username == "" or password == "":
        messagebox.showwarning("Erro", "Preencha todos os campos!")
        return

    # Deixar senha encriptografada
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    try:
        cursor.execute("INSERT INTO usuarios (username, password) VALUES (?, ?)", (username, hashed_password))
        conn.commit()
        messagebox.showinfo("Sucesso", "Usuário registrado com sucesso!")
    except sqlite3.IntegrityError:
        messagebox.showerror("Erro", "Usuário já existe!")

# Função para fazer login
def login_usuario():
    username = entry_username.get()
    password = entry_password.get()

    if username == "" or password == "":
        messagebox.showwarning("Erro", "Preencha todos os campos!")
        return

    cursor.execute("SELECT password FROM usuarios WHERE username = ?", (username,))
    result = cursor.fetchone()

    if result and bcrypt.checkpw(password.encode('utf-8'), result[0]):
        messagebox.showinfo("Sucesso", "Login realizado com sucesso!")
    else:
        messagebox.showerror("Erro", "Usuário ou senha incorretos!")

# Função para limpar os campos
def limpar_campos():
    entry_username.delete(0, ctk.END)
    entry_password.delete(0, ctk.END)

# Interface gráfica usando CustomTkinter
app = ctk.CTk()
app.title("Sistema de Login")
app.geometry("300x400")

label_title = ctk.CTkLabel(app, text="Login e Registro", font=("Arial", 24))
label_title.pack(pady=20)

# Campo nome de usuário
label_username = ctk.CTkLabel(app, text="Usuário")
label_username.pack(pady=10)
entry_username = ctk.CTkEntry(app)
entry_username.pack(pady=10)

# Campo senha
label_password = ctk.CTkLabel(app, text="Senha")
label_password.pack(pady=10)
entry_password = ctk.CTkEntry(app, show="*")
entry_password.pack(pady=10)

# Frame para alinhar botões lado a lado
button_frame = ctk.CTkFrame(app)
button_frame.pack(pady=10)

# Botão de Login
button_login = ctk.CTkButton(button_frame, text="Login", command=login_usuario)
button_login.grid(row=0, column=0, padx=10)

# Botão de Limpar
button_clear = ctk.CTkButton(button_frame, text="Limpar", command=limpar_campos)
button_clear.grid(row=0, column=1, padx=10)

# Botão de Registrar (fica abaixo dos outros dois botões)
button_register = ctk.CTkButton(app, text="Registrar", command=registrar_usuario)
button_register.pack(pady=10)

# Inicia o app
app.mainloop()

# Fecha a conexão com o banco de dados
conn.close()