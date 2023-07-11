import web
import app

render = web.template.render("mvc/views/operador/") #ruta de las vistas

class CambiarHorario: #clase Index
    def GET(self):
        return render.cambiar_horario()