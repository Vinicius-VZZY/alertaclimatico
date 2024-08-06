from flask import Flask, jsonify, request

app = Flask(__name__)

# Inicializar variáveis para armazenamento de dados
dados_usuarios = [
    {'id': 1, 'nome': 'Vinicius Guimarães', 'email': 'viniciusgurquiza@gmail.com', 'telefone': '81 995658341', 'cpf': '09825515414', 'endereco': 'rua da braba, 77', 'Senha': '12345677'}
]
incidentes_relatados = []

# Funções para manipulação de dados
@app.route('/verificar_usuarios', methods=['GET'])
def verificar_usuarios():
    print(jsonify(dados_usuarios))
    return jsonify(dados_usuarios)


# Funções para manipulação de dados
@app.route('/dados_usuarios', methods=['GET'])
def consultar_usuarios():
    return jsonify(dados_usuarios)

@app.route('/dados_usuarios/<int:id>', methods=['GET'])
def consultar_usuarios_por_id(id):
    for usuario in dados_usuarios:
        if usuario.get('id') == id:
            return jsonify(usuario)
    return jsonify({"mensagem": "Usuário não encontrado"})

@app.route('/dados_usuarios', methods=['POST'])
def cadastrar_usuario():
    novo_usuario = request.get_json()
    dados_usuarios.append(novo_usuario)
    return jsonify(dados_usuarios)

@app.route('/dados_usuarios/<int:id>', methods=['PUT'])
def atualizar_usuario(id):
    usuario_atualizado = request.get_json()
    for indice, usuario in enumerate(dados_usuarios):
        if usuario.get('id') == id:
            dados_usuarios[indice].update(usuario_atualizado)
            return jsonify(dados_usuarios[indice])
    return jsonify({"mensagem": "Usuário não encontrado"})

@app.route('/dados_usuarios/<int:id>', methods=['DELETE'])
def excluir_usuario_por_id(id):
    for indice, usuario in enumerate(dados_usuarios):
        if usuario.get('id') == id:
            del dados_usuarios[indice]
            return jsonify(dados_usuarios)
    return jsonify({"mensagem": "Usuário não encontrado"})

if __name__ == '__main__':
    app.run()
    import multiprocessing
    p = multiprocessing.Process(target=app.run, args=('localhost', 8080, True))
    p.start()