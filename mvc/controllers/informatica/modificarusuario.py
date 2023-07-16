import web
import app
import pyrebase
import firebase_config as token

render = web.template.render("mvc/views/informatica/") #ruta de las vistas
firebase = pyrebase.initialize_app(token.firebaseConfig)
auth = firebase.auth() #verifica la conexión a firebase
db = firebase.database()

class ModificarUsuario: #clase Index
    def GET(self):
        users = db.child('data').child('usuarios').get()
        return render.modificar_usuario(users)
    def POST(self):
        try:
            #obtiene los datos del formulario
            formulario = web.input()
            id = formulario['id']
            no_control = formulario['inputControl14']
            nivel = formulario['nivel']
            data = { #crea el diccionario data
                'nivel': nivel,
                'no_control': no_control,
            }
            db.child('data').child('usuarios').child(id).update(data) #actualiza los datos del usuario
            return web.seeother('/informatica/modificar-usuario') #redirecciona a la pagina de usuarios
        except Exception as error:
            users = db.child('data').child('usuarios').get()
            print("Error modificar_usuario POST: {}".format(error.args))
            return render.modificar_usuario(users)