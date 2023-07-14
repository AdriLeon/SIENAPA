import web
import pyrebase
import firebase_config as token
import app as app
import json
import random

render = web.template.render("mvc/views/admin/") #ruta de las vistas

class GenerarPozo: #clase Index
    def GET(self):
        try:
            return render.generar_pozo()
        except Exception as error:
            print("Error GenerarPozo.GET: {}".format(error))
    def POST(self):
        try:
            firebase = pyrebase.initialize_app(token.firebaseConfig)
            db = firebase.database()
            formulario = web.input()
            nombre = formulario.nombre
            convenio = formulario.convenio
            concesion = formulario.concesion
            ubicacion = formulario.ubicacion
            informacion = formulario.informacion
            numero = random.randint(1000, 2000)
            idpozo = hex(numero)
            data = {
                "concesion": concesion,
                "convenio": convenio,
                "informacion": informacion,
                "nombre": nombre,
                "ubicacion": ubicacion,
                "estado_pozo": {
                    "electricidad": 0,
                    "estado": 0,
                    "fallas": 0,
                    "id_falla": 0,
                    "t_activo": 0,
                    "tiempo": "2022-07-23 13:10:11"
                },
                "horario": {
                    "dia1": 0,
                    "dia2": 0,
                    "dia3": 0,
                    "dia4": 0,
                    "dia5": 0,
                    "dia6": 0,
                    "dia7": 0,
                    "h_apagado": "13:10:11",
                    "h_encendido": "13:10:11"
                }
            }
            db.child("data").child("pozos").child(idpozo).set(data)
            return web.seeother("/admin/generar-pozo")

        except Exception as error:
            format = json.loads(error.args[1])
            error = format['error']
            message = error['message']
            print("Error GenerarPozo.POST: {}".format(message))
            web.setcookie('localId', '', 3600)
            return render.generarpozo(message)