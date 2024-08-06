
# Projeto de Desenvolvimento da Aplicação de Monitoramento, Alerta e Reporte de Condições Climáticas

#### Uma breve descrição sobre o que esse projeto faz e para quem ele é:

Essa aplicação tem como função integrar alertas climáticos e localização GPS de maneira interativa para o usuário ter a função Criar Reportes indicando locais onde podem estar ocorrendos deslisamentos, alagamentos, queda de árvores ou de postes de eletricidade/telefonia, etc. Utilizando, e com isso atualizando, os banco de dados de áreas de risco e locais de maior incindência de alagamentos ou deslisamentos que estejam disponíveis ao público pela defesa civil e órgãos de serviços emergenciais. O objetivo é facilitar a divulgação de alertas de emergências climáticas com alertas e notificações para regiões definidas pelo usuário. 

### Apresentação
Nessa aplicação tivemos a ideia de usar o framework Flask para criar um servidor que use os processos API RESTful de método CRUD para armazenar os dados de cadastro dos usuários (pela limitação da equipe/turma no assunto Banco de Dados, essa será uma implementação posterior do projeto). E optamos pela biblioteca Tkinter para criar uma interface gráfica responsiva para o uso. 

### Tkinter

Este script é uma simples aplicação gráfica usando a biblioteca tkinter do Python. Ela é dividida em três telas: "Login", "Início" e "Cadastro".

Na tela "Login", o usuário pode inserir seu nome de usuário e senha para realizar o login. Caso o usuário ainda não tenha cadastro, ele pode clicar no botão "Cadastre-se" para ser redirecionado para a tela de cadastro.

Na tela "Cadastro", o usuário pode inserir seus dados pessoais, como nome, CPF, endereço e telefone, para se cadastrar. Após preencher todos os campos, o usuário pode clicar no botão "Cadastrar" para realizar o cadastro.

Na tela "Início", o usuário pode realizar um teste de alerta climático clicando no botão "Realizar Teste". O resultado do teste será exibido abaixo do botão.

Para criar a interface gráfica, o script utiliza a classe App que herda da classe tk.Tk do tkinter. A tela é inicializada com o título "Alerta Climático" e tamanho de 400x600 pixels. A tela é dividida em três frames, um para cada tela, e são adicionados à uma guia (notebook) usando o método add.

Cada frame é criado com o método ttk.Frame e os widgets são adicionados a ele usando o método pack com a opção fill="x" e expand=True para preencher a tela inteira horizontalmente.

Os widgets utilizados são:

ttk.Label: para exibir texto estático
ttk.Entry: para inserir texto
ttk.Button: para realizar ações quando clicado
ttk.Notebook: para criar guias com várias telas
tkinter.messagebox: para exibir mensagens de alerta ou informação
Para realizar a lógica de negócio, como validar os dados de login ou cadastro, é necessário adicionar a lógica nos métodos login, cadastrar_usuario e cadastrar.# alertaclimatico

### Flask


Baseado no que vimos em sala decidimos usar para armazenar e validar os dados de cadastro e de incidentes um servidor Flask aplicando o método CRUD. 





### Google Maps API
Google maps é a API de mapas escolhida pelo grupo para exibir ao usuário, na interface, o retorno da pesquisa da localidade escolhida.
```
import googlemaps
from datetime import datetime

gmaps = googlemaps.Client(key='Add Your Key here')

# Geocoding an address
geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')

# Look up an address with reverse geocoding
reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))

# Request directions via public transit
now = datetime.now()
directions_result = gmaps.directions("Sydney Town Hall",
                                     "Parramatta, NSW",
                                     mode="transit",
                                     departure_time=now)

# Validate an address with address validation
addressvalidation_result =  gmaps.addressvalidation(['1600 Amphitheatre Pk'], 
                                                    regionCode='US',
                                                    locality='Mountain View', 
                                                    enableUspsCass=True)

# Get an Address Descriptor of a location in the reverse geocoding response
address_descriptor_result = gmaps.reverse_geocode((40.714224, -73.961452), enable_address_descriptor=True)
```




### cep via 
via cep define a localizaçao da busca do usuario 
'''
import requests

api_key = "a17aa54959a46a52dc3c4a2508cbc211"
cidade = "recife"
link = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={api_key}&lang=pt_br"

# Faz a requisição
requisicao = requests.get(link)

# Verifica o status da requisição
if requisicao.status_code == 200:
    dados = requisicao.json()
    print("Dados do tempo:", dados)
elif requisicao.status_code == 400:
    print("Requisição incorreta. Verifique a URL e parâmetros.")
elif requisicao.status_code == 401:
    print("Credenciais inválidas. Verifique sua chave API.")
elif requisicao.status_code == 404:
    print("Cidade não encontrada. Verifique o nome da cidade.")
else:
    print(f"Erro inesperado: {requisicao.status_code}")
print(requisicao.json())

requisicao_dic = requisicao.json()

descricao = requisicao_dic['weather'][0]['description']

temperatura = requisicao_dic['main']['temp']
print ('description', temperatura)

cidade = "recife"
link = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={api_key}&lang=pt_br"
requisicao = requests.get(link)
requisicao_dic = requisicao.json()

# descricao = requisicao_dic['weatrer'][0]['description']
pritemperatura = requisicao_dic['main']['temp'] - 289.15
print('descricao', temperatura)

print(descricao, round(temperatura,2))

print(descricao, f'{round(temperatura,2)}°C')
```




### Validação de usuario.
a minha pesquisa foi para validar e salvar os dados de cadastro dos usuarios, abaixo vai o codigo.

```
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
'''






### Tema

### Tema
