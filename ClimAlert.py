import requests
import re
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox

# Executar a interface Tkinter no processo principal
janela = tk.Tk()

# Código da interface Tkinter

# Título
janela.title("ClimAlert APP")

# Tamanho da janela
janela.geometry("600x800")
janela.minsize(600, 800)

# Definir o layout
frame = tk.Frame(janela)

# Adicionar frame à janela
frame.pack()

# Criar notebook com abas
notebook = ttk.Notebook(frame)
notebook.grid()

# Criar abas
login = tk.Frame(notebook)
cadastro = tk.Frame(notebook)
inicio = tk.Frame(notebook)
resultados = tk.Frame(notebook)
# Adicionar abas ao notebook
notebook.add(login, text="Login")
notebook.add(cadastro, text="Cadastro")
notebook.add(inicio, text="Início")

# Variáveis globais
entry_usuario = None
entry_senha = None
entry_email = None
entry_telefone = None
entry_cpf = None
entry_endereco = None
entry_senha = None

# Label e entrada para Login
def tela_login():
    global entry_usuario
    global entry_senha
    label_usuario = tk.Label(login, text='Usuário')
    label_usuario.grid(row=0, column=0, padx=10, pady=10)

    entry_usuario = tk.Entry(login)
    entry_usuario.grid(row=0, column=1, padx=10, pady=10)

    # Label e entrada para senha
    label_senha = tk.Label(login, text='Senha')
    label_senha.grid(row=0, column=3, padx=10, pady=10)

    entry_senha = tk.Entry(login, show='*')
    entry_senha.grid(row=0, column=4, padx=10, pady=10)

    # Função para ir para a aba de início
    def ir_para_inicio():
        notebook.select(inicio)

    # Botão para login
    botao_login = tk.Button(login, text="Login", command=ir_para_inicio)
    botao_login.grid(row=6, column=4, padx=10, pady=10)

    def ir_para_cadastro():
        notebook.select(cadastro)

    # Botão para cadastro
    botao_cadastro = tk.Button(login, text="Cadastro", command=ir_para_cadastro)
    botao_cadastro.grid(row=6, column=1, padx=10, pady=10)

tela_login()


# Função para validar o login
def tela_cadastro():
    global entry_nome
    global entry_email
    global entry_telefone
    global entry_cpf
    global entry_endereco
    global entry_senha
    global entry_usuario

    label_nome = tk.Label(cadastro, text='Nome Completo:')
    label_nome.grid(row=0, column=0, padx=10, pady=10)
    entry_nome = tk.Entry(cadastro)
    entry_nome.grid(row=0, column=1, padx=10, pady=10)

    label_email = tk.Label(cadastro, text='Email (Usuário):')
    label_email.grid(row=1, column=0, padx=10, pady=10)
    entry_email = tk.Entry(cadastro)
    entry_email.grid(row=1, column=1, padx=10, pady=10)

    label_telefone = tk.Label(cadastro, text='Telefone:')
    label_telefone.grid(row=2, column=0, padx=10, pady=10)
    entry_telefone = tk.Entry(cadastro)
    entry_telefone.grid(row=2, column=1, padx=10, pady=10)

    label_cpf = tk.Label(cadastro, text='CPF:')
    label_cpf.grid(row=3, column=0, padx=10, pady=10)
    entry_cpf = tk.Entry(cadastro)
    entry_cpf.grid(row=3, column=1, padx=10, pady=10)

    label_endereco = tk.Label(cadastro, text='Endereço:')
    label_endereco.grid(row=4, column=0, padx=10, pady=10)
    entry_endereco = tk.Entry(cadastro)
    entry_endereco.grid(row=4, column=1, padx=10, pady=10)

    label_senha = tk.Label(cadastro, text='Senha:')
    label_senha.grid(row=5, column=0, padx=10, pady=10)
    entry_senha = tk.Entry(cadastro, show='*')
    entry_senha.grid(row=5, column=1, padx=10, pady=10)
# Função para validar o nome
def validar_nome(nome):
    if len(nome) < 3:
        return False
    return True

# Função para validar o email
def validar_email(email):
    padrao = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    if re.match(padrao, email):
        return True
    return False

# Função para validar o telefone
def validar_telefone(telefone):
    padrao = r"^\d{11}$"
    if re.match(padrao, telefone):
        return True
    return False

# Função para validar o CPF
def validar_cpf(cpf):
    padrao = r"^\d{11}$"
    if re.match(padrao, cpf):
        return True
    return False

# Função para validar o endereço
def validar_endereco(endereco):
    if len(endereco) < 5:
        return False
    return True

# Função para validar a senha
def validar_senha(senha):
    if len(senha) < 8:
        return False
    return True

# Função para enviar os dados
def enviar_dados():
    nome = entry_nome.get()
    email = entry_email.get()
    telefone = entry_telefone.get()
    cpf = entry_cpf.get()
    endereco = entry_endereco.get()
    senha = entry_senha.get()

    if not validar_nome(nome):
        messagebox.showerror("Erro", "Nome inválido. Por favor, insira um nome com pelo menos 3 caracteres.", icon="error", parent=janela)
        return
    if not validar_email(email):
        messagebox.showerror("Erro", "Email inválido. Por favor, insira um email válido.", icon="error", parent=janela)
        return
    if not validar_telefone(telefone):
        messagebox.showerror("Erro", "Telefone inválido. Por favor, insira um telefone com 11 dígitos.", icon="error", parent=janela)
        return
    if not validar_cpf(cpf):
        messagebox.showerror("Erro", "CPF inválido. Por favor, insira um CPF com 11 dígitos.", icon="error", parent=janela)
        return
    if not validar_endereco(endereco):
        messagebox.showerror("Erro", "Endereço inválido. Por favor, insira um endereço com pelo menos 5 caracteres.", icon="error", parent=janela)
        return
    if not validar_senha(senha):
        messagebox.showerror("Erro", "Senha inválida. Por favor, insira uma senha com pelo menos 8 caracteres.", icon="error", parent=janela)
        return

    dados = {
        "nome": nome,
        "email": email,
        "telefone": telefone,
        "cpf": cpf,
        "endereco": endereco,
        "senha": senha
    }

    resposta = requests.put("http://localhost:8080/usuarios", json=dados)

    if resposta.status_code == 200:
        messagebox.showinfo("Sucesso", "Dados enviados com sucesso!", parent=janela)
    else:
        messagebox.showerror("Erro", "Erro ao enviar dados: " + resposta.text, icon="error", parent=janela)


botao_enviar = tk.Button(cadastro, text="Enviar", command=enviar_dados)
botao_enviar.grid(row=6, column=1, padx=10, pady=10)

tela_cadastro()

# Manter a janela aberta
janela.mainloop()