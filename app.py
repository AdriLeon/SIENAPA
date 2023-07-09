import web

urls = (
    '/', 'mvc.controllers.public.login.Login',
    '/admin/lista_pozos', 'mvc.controllers.admin.listapozos.ListaPozos',
    '/admin/generar_pozo', 'mvc.controllers.admin.generarpozo.GenerarPozo',
    '/admin/cambiar_horario', 'mvc.controllers.admin.cambiarhorario.CambiarHorario',
    '/admin/control_pozo', 'mvc.controllers.admin.controlpozo.ControlPozo',
    '/admin/lista_usuarios', 'mvc.controllers.admin.listausuarios.ListaUsuarios',
    '/admin/generar_reporte', 'mvc.controllers.admin.generarreporte.GenerarReporte',
    '/logout', 'mvc.controllers.admin.logout.Logout',
    '/operador/cambiar_horario', 'mvc.controllers.operador.cambiarhorario.CambiarHorario',
    '/operador/control_pozo', 'mvc.controllers.operador.controlpozo.ControlPozo',
    '/operador/generar_reporte', 'mvc.controllers.operador.generarreporte.GenerarReporte',
    '/operador/lista_pozo', 'mvc.controllers.operador.listapozo.ListaPozo',
    '/operador/lista_usuarios', 'mvc.controllers.operador.listausuarios.ListaUsuarios',
    '/logout', 'mvc.controllers.operador.logout.Logout',
    '/informatica/agregar_usuario', 'mvc.controllers.informatica.agregarusuario.AgregarUsuario',
    '/informatica/modificar_usuario', 'mvc.controllers.informatica.modificarusuario.ModificarUsuario',
    '/logout', 'mvc.controllers.informatica.logout.Logout',
)

app = web.application(urls, globals())

if name == "main":
    web.config.debug = False
    app.run()