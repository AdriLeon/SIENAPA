import web
<<<<<<< HEAD
import app

render = web.template.render("mvc/views/admin/") #ruta de las vistas

class CambiarHorario: #clase Index
    def GET(self):
        return render.cambiar_horario()
=======

urls = (
    '/admin/cambiar_horario', 'mvc.controllers.admin.cambiar_horario.CambiarHorario',
)

class CambiarHorario:
    def GET(self):
        Cambiar_Horario = "Cambiar Horario"
        return render.cambiar_horario()

app = web.application(urls, globals())
render = web.template.render('mvc/views/admin')

if __name__ == '__main__':
    app.run()
>>>>>>> 06e91c54030dc32fdbe749d141941f2d77dfb3a6
