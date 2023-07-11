import web
import app

render = web.template.render("mvc/views/operador/") #ruta de las vistas

class ListaPozo: #clase Index
    def GET(self):
        return render.lista_pozos()