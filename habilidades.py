from flask_restful import Resource

lista_habilidade = ['Python', 'JS', 'HTML', 'CSS'] 

class Habilidades(Resource):
  def get(self):
    return lista_habilidade
