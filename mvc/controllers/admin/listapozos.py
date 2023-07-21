import web
import app
import pyrebase
import firebase_config as token
import json
from datetime import datetime

render = web.template.render("mvc/views/admin/") #ruta de las vistas
firebase = pyrebase.initialize_app(token.firebaseConfig)
auth = firebase.auth() #verifica la conexión a firebase
db = firebase.database()

class ListaPozos: #clase Index
    def GET(self):
        pozos = db.child('data').child('pozos').get()
        return render.lista_pozos(pozos)
