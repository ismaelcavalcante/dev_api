from flask import Flask, request
from flask_restful import Resource, Api
import json
from habilidades import Lista_habilidades, Modificar_habilidades

app = Flask(__name__)
api = Api(app)

desenvolvedores = [
    {'id': 0,
     'nome': 'Ismael',
     'habilidades': ['Python', 'JavaScript', 'Java']
     },
    {'id': 1,
     'nome': 'Galleanni',
     'habilidades': ['Python', 'Django']}
]
# devolve um desenvolvedor pelo ID, também altera e deleta um desenvolvedor
class Desenvolvedor(Resource):
    def get(self, id):
        try:
            response = desenvolvedores[id]
        except IndexError:
            response = {'status': 'Erro', 'mensagem': f'Desenvolvedor de ID {id} não existe!'}
        except Exception:
            response = {'status': 'Erro Desconhecido', 'mensagem': 'Procure o Administrador da API'}
        return response

    def put(self, id):
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return dados

    def delete(self, id):
        desenvolvedores.pop(id)
        return {'status': 'sucesso', 'mensagem': 'Registro Excluído'}

# lista todos os desenvolvedores e permite registar um novo desenvolvedor
class Lista_desenvolvedores(Resource):
    def get(self):
        return desenvolvedores

    def post(self):
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return {'status': 'sucesso', 'mensagem': 'Registro Inserido'}


api.add_resource(Desenvolvedor, '/dev/<int:id>/')
api.add_resource(Lista_desenvolvedores, '/dev/')
api.add_resource(Lista_habilidades, '/habilidades/')
api.add_resource(Modificar_habilidades, '/habilidades/<int:id>/')

if __name__ == '__main__':
    app.run(debug=True)