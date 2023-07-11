import web
import app

render = web.template.render("mvc/views/informatica/") #ruta de las vistas

class AgregarUsuario: #clase Index
    def GET(self):
        return render.agregar_usuario()