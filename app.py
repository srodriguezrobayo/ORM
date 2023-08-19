from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#configuracion de la base de datos
USER_DB='root'
PASS_DB= ''
URL_DB='127.0.0.1'
NAME_DB='flask_sqlarchemy'
FULL_URL_DB = f'mysql://{USER_DB}:{PASS_DB}@{URL_DB}/{NAME_DB}'

app.config ['SQLALCHEMY_DATABASE_URL']=FULL_URL_DB
app.config ['SQLALCHEMY_TRACK_MODYFICATIONS']=False

db=SQLAlchemy(app)

migrate=Migrate()
migrate.init_app(app, db)

class Person(db.model):
    id = db.Column(db.Integer,primary_key=True)
    nombre = db.Column(db.String(250))
    apellido = db.Column(db.String(250))
    correo = db.Column(db.String(250))
    def __int__(self,id,nombre,apellido,correo):
        self.id=id
        self.nombr=nombre
        self.apellido=apellido
        self.correo=correo
    def json(self):
        return {'id':self.id,'nombre':self.nombre,'apellido':self.apellido,'correo':self.correo}
    def __str__(self):
        return str(self.__class__)+":"+str(self.__dict__)
    
