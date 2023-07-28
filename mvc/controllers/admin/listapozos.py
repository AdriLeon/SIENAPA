import web
import app
import pyrebase
import firebase_config as token
import json
from datetime import datetime

render = web.template.render("mvc/views/admin/") #ruta de las vistas
firebase = pyrebase.initialize_app(token.firebaseConfig)
auth = firebase.auth() 
db = firebase.database()


class ListaPozos: #clase Index
    def GET(self):
        try:
            cookie = web.cookies().get("localid") # almacena los datos de la cookie
            users = db.child('data').child('usuarios').get()
            for user in users.each():
                    if user.key() == cookie and user.val().get('status') == 'activo':
                        if user.val()['nivel'] == 'administrador':
                            return render.generar_pozo()
                        elif user.val()['nivel'] in ['operador', 'informatica']:
                            web.setcookie('localid', None)
                            return web.seeother('/logout')
                        else:
                            web.setcookie('localid', None)
                            return web.seeother('/logout')
            web.setcookie('localid', None)
            return web.seeother('/logout')
        except Exception as e:
            # Manejo de errores en caso de que ocurra una excepción
            return "Ocurrió un error: " + str(e)
