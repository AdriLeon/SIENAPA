import web
import app
import pyrebase
import firebase_config as token
import json
from datetime import datetime

render = web.template.render("mvc/views/operador/") #ruta de las vistas
firebase = pyrebase.initialize_app(token.firebaseConfig)
auth = firebase.auth() #verifica la conexión a firebase
db = firebase.database()

class ControlPozo: #clase Index
    def GET(self):
        cookie = web.cookies().get("localid") #almacena los datos de la cookie
        users = db.child('data').child('usuarios').get()
        pozos = db.child('data').child('pozos').get()
        for user in users.each():
            if user.key() == cookie and user.val()['nivel'] == 'administrador':
                return web.seeother('/logout')
            elif user.key() == cookie and user.val()['nivel'] == 'operador':
                web.setcookie('localid', None)
                return render.control_pozo(pozos)
            elif user.key() == cookie and user.val()['nivel'] == 'informatica':
                web.setcookie('localid', None)
                return web.seeother('/logout')
        web.setcookie('localid', None)
        return web.seeother('/logout')