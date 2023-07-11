import web
import app

render = web.template.render("mvc/views/operador/") #ruta de las vistas

class ListaUsuarios: #clase Index
    def GET(self):
        return render.lista_usuarios()