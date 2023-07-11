import web
import app

render = web.template.render("mvc/views/informatica/") #ruta de las vistas

class ModificarUsuario: #clase Index
    def GET(self):
        return render.modificar_usuario()