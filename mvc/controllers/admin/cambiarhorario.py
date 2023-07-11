import web

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
