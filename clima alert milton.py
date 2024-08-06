import requests
import re
import tkinter as tk
import tkinter.ttk as ttk

# Executar a interface Tkinter no processo principal
janela = tk.Tk()

# Codigo da interface Tkinter

# Titulo
janela.title("ClimAlert APP")

# Tamanho da janela
janela.geometry("600x800")
janela.minsize(600, 800)

# Definir o layout
frame = tk.Frame(janela)

# Adicionar frame a janela
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
notebook.add(inicio, text="Inicio")

# Variaveis globais
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
    label_usuario = tk.Label(login, text='Usuario')
    label_usuario.grid(row=0, column=0, padx=10, pady=10)

    entry_usuario = tk.Entry(login)
    entry_usuario.grid(row=0, column=1, padx=10, pady=10)

    # Label e entrada para senha
    label_senha = tk.Label(login, text='Senha')
    label_senha.grid(row=0, column=3, padx=10, pady=10)

    entry_senha = tk.Entry(login, show='*')
    entry_senha.grid(row=0, column=4, padx=10, pady=10)

    # Funcao para ir para a aba de inicio
    def ir_para_inicio():
        notebook.select(inicio)

    # Botao para login
    botao_login = tk.Button(login, text="Login", command=ir_para_inicio)
    botao_login.grid(row=6, column=4, padx=10, pady=10)

    def ir_para_cadastro():
        notebook.select(cadastro)

    # Botao para cadastro
    botao_cadastro = tk.Button(login, text="Cadastro", command=ir_para_cadastro)
    botao_cadastro.grid(row=6, column=1, padx=10, pady=10)

tela_login()


# Funcao para validar o login
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

    label_email = tk.Label(cadastro, text='Email (Usuario):')
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

    label_endereco = tk.Label(cadastro, text='Endereco:')
    label_endereco.grid(row=4, column=0, padx=10, pady=10)
    entry_endereco = tk.Entry(cadastro)
    entry_endereco.grid(row=4, column=1, padx=10, pady=10)

    label_senha = tk.Label(cadastro, text='Senha:')
    label_senha.grid(row=5, column=0, padx=10, pady=10)
    entry_senha = tk.Entry(cadastro, show='*')
    entry_senha.grid(row=5, column=1, padx=10, pady=10)
# Funcao para validar o nome
def validar_nome(nome):
    if len(nome) < 3:
        return False
    return True

# Funcao para validar o email
def validar_email(email):
    padrao = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    if re.match(padrao, email):
        return True
    return False

# Funcao para validar o telefone
def validar_telefone(telefone):
    padrao = r"^\d{11}$"
    if re.match(padrao, telefone):
        return True
    return False

# Funcao para validar o CPF
def validar_cpf(cpf):
    padrao = r"^\d{11}$"
    if re.match(padrao, cpf):
        return True
    return False

# Funcao para validar o endereco
def validar_endereco(endereco):
    if len(endereco) < 5:
        return False
    return True

# Funcao para validar a senha
def validar_senha(senha):
    if len(senha) < 8:
        return False
    return True

# Funcao para enviar os dados
def enviar_dados():
    nome = entry_nome.get()
    email = entry_email.get()
    telefone = entry_telefone.get()
    cpf = entry_cpf.get()
    endereco = entry_endereco.get()
    senha = entry_senha.get()

    if not validar_nome(nome):
        print("Nome invalido. Por favor, insira um nome com pelo menos 3 caracteres.")
        return
    if not validar_email(email):
        print("Email invalido. Por favor, insira um email valido.")
        return
    if not validar_telefone(telefone):
        print("Telefone invalido. Por favor, insira um telefone com 11 digitos.")
        return
    if not validar_cpf(cpf):
        print("CPF invalido. Por favor, insira um CPF com 11 digitos.")
        return
    if not validar_endereco(endereco):
        print("Endereco invalido. Por favor, insira um endereco com pelo menos 5 caracteres.")
        return
    if not validar_senha(senha):
        print("Senha invalida. Por favor, insira uma senha com pelo menos 8 caracteres.")
        return

    dados = {
        "nome": nome,
        "email": email,
        "telefone": telefone,
        "cpf": cpf,
        "endereco": endereco,
        "senha": senha
    }

    resposta = requests.post("http://localhost:5000/dados_usuarios", json=dados)

    if resposta.status_code == 200:
        print("Dados enviados com sucesso!")
    else:
        print("Erro ao enviar dados:", resposta.text)
        print("Status code:", resposta.status_code)

botao_enviar = tk.Button(cadastro, text="Enviar", command=enviar_dados)
botao_enviar.grid(row=6, column=1, padx=10, pady=10)

tela_cadastro()

# Manter a janela aberta
janela.mainloop()