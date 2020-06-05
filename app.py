from flask import Flask, jsonify, request
import json

app = Flask(__name__)

desenvolvedores = [
  {'id':'0',
   'nome':'Renoir',
   'habilidades':['Python', 'Flask']},
  {'id':'1',
   'nome':'Joao',
   'habilidades':['HTML','CSS']}
]

# Retorna dev por id, deleta e altera
@app.route('/dev/<int:id>/', methods=['GET', 'PUT', 'DELETE'])
def desenvolvedor(id):
  if request.method == 'GET':
    try:
      response = desenvolvedores[id]
    except IndexError:
      mensagem = 'Desenvolvedor de id {} nao existe'.format(id)
      response = {'status':'erro', 'mensagem':mensagem}
    except Exception:
      mensagem = "Erro desconhecido. Procure o administrador da API"
      response = {'status':'erro', 'mensagem':mensagem} 
    return jsonify(response)

  elif request.method == 'PUT':
    dados = json.loads(request.data)
    desenvolvedores[id] = dados
    return jsonify(dados)

  elif request.method == 'DELETE':
    desenvolvedores.pop(id)
    return jsonify ({'status':'sucesso', 'mensagem':'Registro excluido!'})


# Lista dev e registra novo dev
@app.route('/dev/', methods=['POST', 'GET'])
def lista_desenvolvedors():
  if request.method == 'POST':
    dados = json.loads(request.data)
    posicao = len(desenvolvedores)
    dados['id'] = posicao
    desenvolvedores.append(dados)
    return jsonify(desenvolvedores[posicao])

  elif request.method == 'GET':
    return jsonify(desenvolvedores)


if __name__ == '__main__':
  app.run(debug=True)