import os

from json import dumps
from flask import Flask, Response, request
from flask_restful import Api, Resource
from src.sistema_arquivos import FileSystem
from src.validator.validador import validator, get_json_schema

UPLOAD_FOLDER = os.getcwd()

app = Flask(__name__)
api = Api(app)

class Endpoint(Resource):

    @app.route("/api/v1/FileSystem", methods=["POST", "GET", "PUT", "DELETE"])       
    def file_system(*self):

        if request.method == "POST":
            schema: str = "create"
            
            if not validator(request.args, schema):
                return Response(dumps(get_json_schema(schema)), 400, mimetype="application/json")

            file_name: str = request.args["FileName"]
            cpf: str = request.args["CPF"]
            project_id: int = request.args["ProjectID"]
            file: bytes = request.data        

            file_system: FileSystem = FileSystem(cpf, project_id)

            if not file_system.create_file(file_name, file):
                return Response("Falha ao criar o arquivo", 500)

            return Response("Criado", status=201)
            
        elif request.method == "GET":
            schema: str = "read"
            
            if not validator(request.args, schema):
                return Response(dumps(get_json_schema(schema)), 400, mimetype="application/json")
            
            file_name: str = request.args["FileName"]
            cpf: str = request.args["CPF"]  
            project_id: int = request.args["ProjectID"]      

            file_system: FileSystem = FileSystem(cpf, project_id)
            file: bytes = file_system.read_file(file_name)

            if file == None: return Response("Arquivo não encontrado", 404)

            return Response(file, status=200)

        elif request.method == "PUT":
            schema: str = "update"
            
            if not validator(request.args, schema):
                return Response(dumps(get_json_schema(schema)), 400, mimetype="application/json")
            
            file_name: str = request.args["FileName"]
            cpf: str = request.args["CPF"]
            project_id: int = request.args["ProjectID"]
            file: bytes = request.data

            file_system: FileSystem = FileSystem(cpf, project_id)

            if not file_system.update_file(file_name, file):
                return Response("Falha ao alterar o arquivo", 500)

            return Response("Alterado", status=200)

        elif request.method == "DELETE":
            schema: str = "delete"
            
            if not validator(request.args, schema):
                return Response(dumps(get_json_schema(schema)), 400, mimetype="application/json")
            
            file_name: str = request.args["FileName"]
            cpf: str = request.args["CPF"]
            project_id: int = request.args["ProjectID"]        

            file_system: FileSystem = FileSystem(cpf, project_id)

            if not file_system.delete_file(file_name):
                return Response("Falha ao remover o arquivo", 400)

            return Response("Removido", status=200)

    @app.route("/api/v1/FileSystem/ListFiles", methods=["GET"])       
    def list_files():
        schema: str = "list_files"
        
        if not validator(request.args, schema):
            return Response(dumps(get_json_schema(schema)), 400, mimetype="application/json")
                
        cpf: str = request.args["CPF"]   
        project_id: int = request.args["ProjectID"]     

        file_system: FileSystem = FileSystem(cpf, project_id)
        file_list: list = file_system.list_files()

        if file_list == None: return Response([], 404, mimetype="application/json")

        return Response(dumps(file_list), status=200, mimetype="application/json")
    
if __name__ == '__main__':    
    app.run(host='0.0.0.0', port=2000)