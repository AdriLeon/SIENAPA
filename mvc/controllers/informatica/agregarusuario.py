import web
import app
import pyrebase
import firebase_config as token
import json

render = web.template.render("mvc/views/informatica/") #ruta de las vistas
firebase = pyrebase.initialize_app(token.firebaseConfig)
auth = firebase.auth() #verifica la conexión a firebase
db = firebase.database()

class AgregarUsuario: #clase Index
    def GET(self):
        return render.agregar_usuario()
    
    def POST(self):
        try:
            formulario = web.input() #almacena los datos del formulario web
            email = formulario['inputEmail14'] #almacena el email del formulario web
            no_control = formulario['inputControl14'] #almacena el no_control del formulario web
            password = formulario['inputPassword14'] #almacena el password del formulario web
            nivel = formulario['nivel'] #almacena el nivel del formulario web
            user = auth.create_user_with_email_and_password(email, password) #crea el usuario en firebase
            chid = user['localId'] #almacena el id del usuario
            data = { #crea el diccionario data
                'correo': email,
                'nivel': nivel,
                'status': "activo",
                'no_control': no_control,
                'logs': {
                    'actividad': '',
                    'id_logs': '',
                    'tiempo': ''
                }
            }
            db.child('data').child('usuarios').child(user['localId']).set(data) #almacena el diccionario data en la base de datos
            return web.seeother('/informatica/agregar-usuario')
        except Exception as error:
            print("Error agregar_usuario POST: {}".format(error))
            return render.agregar_usuario()