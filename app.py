import os

from json import dumps

from io import BytesIO

from flask import Flask, request, Response, session, send_file
from flask_restful import Resource, Api
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy

UPLOAD_FOLDER = os.getcwd()

app = Flask(__name__)

db = SQLAlchemy(app)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = b'CDgWUjqcCaNURJD9AkcRgKaTucApXBGH'
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = 'filesystem'

api = Api(app)

class Upload(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(50))
    data = db.Column(db.LargeBinary)

class PHAuth(Resource):

    @app.route("/api/v1/FileSystem/Create", methods=["POST"])       
    def Create(*self):
        
        if request.method == 'POST':
            file = request.files['file']

            upload = Upload(filename = file.filename, data = file.read())
            db.session.add(upload)
            db.session.commit()
            
            return f'Uploaded: {file.filename}'
            

        return Response("Autenticado", status=200)
        
    @app.route("/api/v1/FileSystem/Create", methods=["GET"])       
    def Read(upload_id):
        
        upload = Upload.querry.filter_by(id = upload_id).first()

        return send_file(BytesIO(upload.data), attechment_filename = upload.filename, as_attachment=True)
    



if __name__ == '__main__':    
    app.run(host='0.0.0.0', port=2000)