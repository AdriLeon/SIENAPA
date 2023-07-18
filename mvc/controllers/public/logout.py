import web
import app

render = web.template.render("mvc/views/operador/") #ruta de las vistas

class Logout: #clase Index
    def GET(self):
        web.setcookie('localid', None) #establece la cookie en None
        return web.seeother('/')