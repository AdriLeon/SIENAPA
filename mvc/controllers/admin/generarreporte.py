import web
import app as app
import firebase_config as token
from fpdf import FPDF
import pyrebase
from datetime import datetime
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
mes = meses_en_espanol[datetime.now().month]
count = 0
total_fallas = 0
logo = os.path.abspath("static/img/logo.png")

render = web.template.render("mvc/views/admin/") #ruta de las vistas

class GenerarReporte: #clase Index
    def GET(self):
        return render.generar_reporte()
    
    def POST(self):
        try:
            cookie = web.cookies().get("localid") #almacena los datos de la cookie
            pozos = db.child('data').child('pozos').get()
            user = db.child('data').child('usuarios').child(cookie).get()
            formulario = web.input()
            fechaInicio = formulario.fechaInicio
            fechaFin = formulario.fechaFinal
            generarReporte(fechaInicio, fechaFin, pozos, user, cookie)
            print("Total de fallas: {}".format(total_fallas))
            return render.generar_reporte()
        except Exception as error:
            print("Error GenerarReporte.POST: {}".format(error))
            return render.generar_reporte()

    
def generarReporte(fechaInicio, fechaFin, pozos, user, cookie):
    global count
    global total_fallas
    total_fallas = 0
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
    pdf.cell(0, 20, 'Tulancingo de Bravo, Hidalgo a {} de {} del {}'.format(datetime.now().day, mes, datetime.now().year), ln=1, align='R')
    pdf.set_font('helvetica', '', 12)
    pdf.cell(0, 10, ln=1,)
    pdf.cell(0, 0, '**Persona que solicita**: #' + user.val().get('no_control'), ln=1, align='R', markdown=True)
    pdf.cell(0, 20, '**N° de Reporte**: 001', border=False, ln=1, align='R', markdown=True)
    pdf.set_font('helvetica', '', 12)
    pdf.cell(0, 10, ln=1,)
    fechaI_d_m_a_str = datetime.strptime(fechaInicio, "%Y-%m-%d")
    fechaI_d_m_a = fechaI_d_m_a_str.strftime("%d-%m-%Y")
    fechaF_d_m_a_str = datetime.strptime(fechaFin, "%Y-%m-%d")
    fechaF_d_m_a = fechaF_d_m_a_str.strftime("%d-%m-%Y")
    pdf.cell(0, 0, 'Incidencias ocurridas durante el período comprendido entre el **{}** y el **{}**.'.format(str(fechaI_d_m_a), str(fechaF_d_m_a)), ln=1, align='L', markdown=True)        
    pdf.cell(0, 10, ln=1,)

    # Initialize the flag to check if there are any records
    has_records = False
    for pozo in pozos.each():
        fallas = db.child('data').child('pozos').child(pozo.key()).child('fallas').get()
        for falla in fallas.each():
            fecha_hora_str = falla.val().get('tiempo')
            fecha_hora = datetime.strptime(fecha_hora_str, "%Y-%m-%d %H:%M:%S")
            fecha_falla = fecha_hora.strftime("%Y-%m-%d")
            fecha_inicio_str = datetime.strptime(fechaInicio, "%Y-%m-%d")
            fecha_inicio = fecha_inicio_str.strftime("%Y-%m-%d")
            fecha_fin_str = datetime.strptime(fechaFin, "%Y-%m-%d")
            fecha_fin = fecha_fin_str.strftime("%Y-%m-%d")
            if fecha_falla >= fecha_inicio and fecha_falla <= fecha_fin:
                if not has_records:
                    # Generate the name of the well and the table headers only once
                    pdf.cell(0, 20, '**Pozo**: ' + pozo.val().get('nombre'), ln=1, align='C', markdown=True)
                    pdf.cell(0, 0, '**Ubicación del pozo**: ' + pozo.val().get('ubicacion'), ln=1, align='C', markdown=True)
                    pdf.cell(0, 15, ln=1,)
                    pdf.set_font('helvetica', 'B', 12)
                    pdf.cell(0, 16, 'FALLAS', border=True, ln=1, align='C')
                    pdf.set_font('helvetica', '', 12)
                    has_records = True  # Set the flag to True once the headers are generated
                    count += 1
                    total_fallas += 1
                    pdf.cell(30, 20, f'Falla: {count}', border=True, align='L')
                    pdf.cell(116, 20, falla.val().get('falla'), border=True, align='C')
                    pdf.cell(50, 20, falla.val().get('tiempo'), border=True, ln=True, align='C')
                else:
                    has_records = False
                    break
            count = 0  # Reset the count for each pozo
    pdf.output('static/pdf/reporte.pdf')
    return total_fallas
