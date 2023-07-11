import web
import app

render = web.template.render("mvc/views/operador/") #ruta de las vistas

class ControlPozo: #clase Index
    def GET(self):
        return render.control_pozo()