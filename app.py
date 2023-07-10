import web

urls = (
    '/', 'mvc.controllers.public.login.Login',
    '/admin/lista_pozos', 'mvc.controllers.admin.lista_pozos.Lista_Pozos',
    '/admin/generar_pozo', 'mvc.controllers.admin.generar_pozo.Generar_Pozo',
    '/admin/cambiar_horario', 'mvc.controllers.admin.cambiar_horario.Cambiar_Horario',
    '/admin/control_pozo', 'mvc.controllers.admin.control_pozo.Control_Pozo',
    '/admin/lista_usuarios', 'mvc.controllers.admin.lista_usuarios.Lista_Usuarios',
    '/admin/generar_reporte', 'mvc.controllers.admin.generar_reporte.Generar_Reporte',
    '/logout', 'mvc.controllers.admin.logout.Logout',
    '/operador/cambiar_horario', 'mvc.controllers.operador.cambiar_horario.Cambiar_Horario',
    '/operador/control_pozo', 'mvc.controllers.operador.control_pozo.Control_Pozo',
    '/operador/generar_reporte', 'mvc.controllers.operador.generar_reporte.Generar_Reporte',
    '/operador/lista_pozo', 'mvc.controllers.operador.lista_pozo.Lista_Pozo',
    '/operador/lista_usuarios', 'mvc.controllers.operador.lista_usuarios.Lista_Usuarios',
    '/logout', 'mvc.controllers.operador.logout.Logout',
    '/informatica/agregar_usuario', 'mvc.controllers.informatica.agregar_usuario.Agregar_Usuario',
    '/informatica/modificar_usuario', 'mvc.controllers.informatica.modificar_usuario.Modificar_Usuario',
    '/logout', 'mvc.controllers.informatica.logout.Logout',
)

app = web.application(urls, globals())

if __name__ == "__main__":
    web.config.debug = False
    app.run()