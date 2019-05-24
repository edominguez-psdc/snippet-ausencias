from odoo import api, fields, models
import psycopg2 


PSQL_HOST = "localhost"
PSQL_PORT = "5432"
PSQL_USER = "test"
PSQL_PASS = "12345"
PSQL_DB   = "leave12"

# holiday_status_id  date_from  date_to  name
class HolidaysRequest(models.Model):
    _inherit = 'hr.leave'

    def website_form_input(self, request, values):
        try:
            # Conectarse a la base de datos
            connstr = "host=%s port=%s user=%s password=%s dbname=%s" % (PSQL_HOST, PSQL_PORT, PSQL_USER, PSQL_PASS, PSQL_DB)
            conn = psycopg2.connect(connstr)

            # Abrir un cursor para realizar operaciones sobre la base de datos
            cur = conn.cursor()
            query_insert = "INSERT INTO hr_leave(holiday_status_id, date_from, date_to, name) VALUES (DEFAULT,%s,%s,%s,%s)"
            cur.execute(query_insert)

            # Ejecutar una consulta SELECT
            # sqlquery = "select id, name from hr_leave;"
            # cur.execute(sqlquery)

            # Obtener los resultados como objetos Python
            # row = cur.fetchone()

            # Cerrar la conexión con la base de datos
            cur.close()
            conn.close()

            # Recuperar datos del objeto Python
            # username = row[1]

            # Hacer algo con los datos
            # print(username)
            print("Sus datos han sido enviados, se le confirmara por correo su peticion.")
        except:
            print("Error al ingresar sus datos.")