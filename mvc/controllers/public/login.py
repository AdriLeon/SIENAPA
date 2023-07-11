import web
import app

class GenerarReporte: #clase Index
    def POST(self):
        return web.seeother('/admin/lista-pozos')