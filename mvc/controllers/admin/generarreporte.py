import web
import app as app
import firebase_config as token
from fpdf import FPDF
import pyrebase
import datetime as dt
import os

firebase = pyrebase.initialize_app(token.firebaseConfig)
auth = firebase.auth() 
db = firebase.database()

meses_en_espanol = {
    1: "enero",
    2: "febrero",
    3: "marzo",
    4: "abril",
    5: "mayo",
    6: "junio",
    7: "julio",
    8: "agosto",
    9: "septiembre",
    10: "octubre",
    11: "noviembre",
    12: "diciembre",
}
mes = meses_en_espanol[dt.datetime.now().month]
count = 0
logo = os.path.abspath("static/img/logo.png")

render = web.template.render("mvc/views/admin/") #ruta de las vistas

class GenerarReporte: #clase Index
    def GET(self):
        return render.generar_reporte()
    
    def POST(self):
        try:
            cookie = web.cookies().get("localid") #almacena los datos de la cookie
            fallas = db.child('data').child('pozos').child('-N_uYDK-n_t2hdW3nItg').child('fallas').get()
            pozo = db.child('data').child('pozos').child('-N_uYDK-n_t2hdW3nItg').get()
            user = db.child('data').child('usuarios').child(cookie).get()
            formulario = web.input()
            fechaInicio = formulario.fechaInicio
            fechaFin = formulario.fechaFinal
            generarReporte(fechaInicio, fechaFin, fallas, pozo, user, cookie)
            return render.generar_reporte()
        except Exception as error:
            print("Error GenerarReporte.POST: {}".format(error))
            return render.generar_reporte()

    
def generarReporte(fechaInicio, fechaFin, fallas, pozo, user, cookie):
        pdf = FPDF ('P', 'mm', 'Letter')
        pdf.set_auto_page_break(auto=True, margin = 15)
        pdf.add_page()
        pdf.image(logo, 10, 12, 40)
        pdf.set_font('helvetica', '', 12)
        pdf.cell(0, 10, 'COMISIÓN DE AGUA Y ALCANTARILLADO DEL', border=False, ln=1, align='C')
        pdf.cell(0, 2, 'MUNICIPIO DE TULANCINGO DE BRAVO HIDALGO', border=False, ln=1, align='C')
        pdf.set_font('helvetica', 'B', 12)
        pdf.cell(0, 20, 'REPORTE DE FALLAS EN POZOS DE AGUA', border=False, align='C')
        pdf.set_font('helvetica', '', 12)
        pdf.cell(0, 15, ln=1,)
        pdf.cell(0, 20, 'Tulancingo de Bravo, Hidalgo a {} de {} del {}'.format(dt.datetime.now().day, mes, dt.datetime.now().year), ln=1, align='R')
        pdf.set_font('helvetica', '', 12)
        pdf.cell(0, 10, ln=1,)
        pdf.cell(0, 0, '**Persona que solicita**: #' + user.val().get('no_control'), ln=1, align='R', markdown=True)
        pdf.cell(0, 20, '**N° de Reporte**: 001', border=False, ln=1, align='R', markdown=True)
        pdf.set_font('helvetica', '', 12)
        pdf.cell(0, 10, ln=1,)
        pdf.cell(0, 0, 'Incidencias ocurridas durante el período comprendido entre el **{}** y el **{}**.'.format(fechaInicio, fechaFin), ln=1, align='L', markdown=True)
        pdf.cell(0, 10, ln=1,)
        pdf.cell(0, 20, '**Pozo**: '+ pozo.val().get('nombre'), ln=1, align='C', markdown=True)
        pdf.cell(0, 0, '**Ubicación del pozo**: ' + pozo.val().get('ubicacion'), ln=1, align='C', markdown=True)
        pdf.cell(0, 15, ln=1,)
        pdf.set_font('helvetica', 'B', 12)
        pdf.cell(0, 16, 'FALLAS', border=True, ln=1, align='C')
        pdf.set_font('helvetica', '', 12)
        for falla in fallas.each():
            global count
            count += 1
            pdf.cell(30, 20, f'Falla: {count}', border=True, align='L')
            pdf.cell(116, 20, falla.val()['falla'], border=True, align='C')
            pdf.cell(50, 20, falla.val()['tiempo'], border=True, ln=True, align='C')
        pdf.output('static/pdf/reporte.pdf')