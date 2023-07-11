import web
import app

render = web.template.render("mvc/views/admin/") #ruta de las vistas

class ListaUsuarios: #clase Index
    def GET(self):
        return render.listas_usuarios()