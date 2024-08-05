
# Projeto de Desenvolvimento da Aplicação de Monitoramento, Alerta e Reporte de Condições Climáticas

####Uma breve descrição sobre o que esse projeto faz e para quem ele é:

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





### Tema



### Tema



### Tema





### Tema

### Tema
