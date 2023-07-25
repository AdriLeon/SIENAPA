import web
import app as app
import pyrebase
import firebase_config as token
import json

render = web.template.render("mvc/views/operador/") 
firebase = pyrebase.initialize_app(token.firebaseConfig)
auth = firebase.auth() 
db = firebase.database()

class CambiarHorario:
    def GET(self, id_pozo):
        horarios = db.child('data').child('pozos').child(id_pozo).child('horario').get() #obtiene los horarios de la base de datos
        return render.cambiar_hora(id_pozo, horarios)

    def POST(self, id_pozo):
        try:
            formulario = web.input() #almacena los datos del formulario
            time1 = formulario['time1']
            time2 = formulario['time2']
            data = { #crea el diccionario data
                'h_apagado': str(time2),
                'h_encendido': str(time1),
            }
            db.child('data').child('pozos').child(id_pozo).child('horario').update(data) #actualiza los datos del horario
            return web.seeother('/operador/control-pozo') #redirecciona a la pagina de pozos
        except Exception as error:
            horarios = db.child('data').child('pozos').child(id_pozo).child('horario').get()
            print("Error cambiar_horario POST: {}".format(error.args))
            return render.cambiar_hora(id_pozo, horarios)