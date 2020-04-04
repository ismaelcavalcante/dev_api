from flask import request
from flask_restful import Resource
import json

habilidades = ['Java', 'Ruby', 'Python', 'Java', 'JavaScript', 'Php', 'C#', 'C']

# consultar e Inserir Habilidades
class Lista_habilidades(Resource):
    def get(self):
        return habilidades

    def post(self):
        dados = json.loads(request.data)
        habilidades.append(dados)
        return {'status': 'sucesso', 'mensagem': 'Habilidade Inserida'}

#Modificar e Excluir habilidades
class Modificar_habilidades(Resource):
    def put(self, id):
        dados = json.loads(request.data)
        habilidades[id] = dados
        return dados

    def delete(self, id):
        habilidades.pop(id)
        return {'status': 'sucesso', 'mensagem': 'Habilidade Excluída'}