import web
import app
import pyrebase
import firebase_config as token
import json
from datetime import datetime

render = web.template.render("mvc/views/admin/") #ruta de las vistas


class ListaPozos: #clase Index
    def GET(self):
        return render.lista_pozos()
