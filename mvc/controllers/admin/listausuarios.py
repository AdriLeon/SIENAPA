import web
import pyrebase
import firebase_config as token
import app as app
import json

render = web.template.render("mvc/views/admin/") #ruta de las vistas

class ListaUsuarios: #clase Index
    def GET(self):
        try:
            firebase = pyrebase.initialize_app(token.firebaseConfig)
            db = firebase.database()
            users = db.child("data").child("usuarios").get()
            return render.lista_usuarios(users)
        except Exception as error:
            print("Error UsersList.GET: {}".format(error))