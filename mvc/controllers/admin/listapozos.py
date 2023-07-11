import web
import app

render = web.template.render("mvc/views/admin/") #ruta de las vistas

class ListaPozos: #clase Index
    def GET(self):
        return render.lista_pozos()