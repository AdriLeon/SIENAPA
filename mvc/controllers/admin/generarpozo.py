import web
import app

render = web.template.render("mvc/views/admin/") #ruta de las vistas

class GenerarPozo: #clase Index
    def GET(self):
        return render.generar_pozo()