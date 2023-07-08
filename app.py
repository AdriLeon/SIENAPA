import web

urls = (
    '/', 'mvc.controllers.public.login.Login',
    '/admin/lista-pozos', 'mvc.controllers.admin.lista-pozos.Lista-pozos',
    '/admin/generar-pozo', 'mvc.controllers.admin.generar-pozo.Generar-pozo',
    '/admin/cambiar-horario', 'mvc.controllers.admin.cambiar-horario.Cambiar-horario',
    '/admin/control-pozo', 'mvc.controllers.admin.control-pozo.Control-pozo',
    '/admin/lista-usuarios', 'mvc.controllers.admin.lista-usuarios.Lista-usuarios',
    '/admin/generar-reporte', 'mvc.controllers.admin.generar-reporte.Generar-reporte',
    '/logout', 'mvc.controllers.admin.logout.Logout',
    '/operador/cambiar-horario', 'mvc.controllers.operador.cambiar-horario.Cambiar-horario',
    '/operador/control-pozo', 'mvc.controllers.operador.control-pozo.Control-pozo',
    '/operador/generar-reporte', 'mvc.controllers.operador.generar-reporte.Generar-reporte',
    '/operador/lista-pozo', 'mvc.controllers.operador.lista-pozo.Lista-pozo',
    '/operador/lista-usuarios', 'mvc.controllers.operador.lista-usuarios.Lista-usuarios',
    '/logout', 'mvc.controllers.operador.logout.Logout',
    '/informatica/agregar-usuario', 'mvc.controllers.informatica.agregar-usuario.Agregar-usuario',
    '/informatica/modificar-usuario', 'mvc.controllers.informatica.modificar-usuario.Modificar-usuario',
    '/logout', 'mvc.controllers.informatica.logout.Logout',
)

app = web.application(urls, globals())

if __name__ == "__main__":
    web.config.debug = False
    app.run()