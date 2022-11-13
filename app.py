import os

from json import dumps

from flask import Flask, Response, request
from flask_restful import Api, Resource


UPLOAD_FOLDER = os.getcwd()

app = Flask(__name__)


app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = b'CDgWUjqcCaNURJD9AkcRgKaTucApXBGH'
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = 'filesystem'

api = Api(app)

Data = "C:/Users/José/Desktop/Facul/TCC/Data/44555756851"

os.chdir(Data)

class PHAuth(Resource):

    @app.route("/api/v1/FileSystem/Create", methods=["POST"])       
    def Create(*self):
        
        with open("cpf.txt", "x") as file:
            os.rename(file)

        return Response("Autenticado", status=200)
        
    @app.route("/api/v1/FileSystem/Read", methods=["GET"])       
    def Read(*self):
        
        with open("cpf.txt", "r", "Data") as file:
            print(file.read())

        return Response("Autenticado", status = 200)

    @app.route("/api/v1/FileSystem/Update", methods = ["POST"])
    def Update(*self):

        with open("file.txt", "w") as file:
            file.write("jesus")

        return Response("Autenticado", status = 200)

    @app.route("/api/v1/FileSystem/Delete", methods = ["DELETE"])
    def Delete(*self):

        if os.path.exists("file.txt"):
            os.remove("file.txt")
        else:
            print ("the file does not exist")

        return Response("Autenticado", status = 200)

if __name__ == '__main__':    
    app.run(host='0.0.0.0', port=2000)