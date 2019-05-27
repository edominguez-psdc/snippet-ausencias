from odoo import api, fields, models
import psycopg2 



# holiday_status_id  date_from  date_to  name
class HolidaysRequest(models.Model):
    _inherit = 'hr.leave'

    PSQL_HOST = "107.0.0.1"
    PSQL_PORT = "5432"
    PSQL_USER = "test"
    PSQL_PASS = "12345"
    PSQL_DB   = "leave12"

    @api.multi
    def website_form_input(self):
        try:
            # Conectarse a la base de datos
            connstr = "user=%s password=%s host=%s port=%s dbname=%s" % (PSQL_USER, PSQL_PASS, PSQL_HOST, PSQL_PORT, PSQL_DB)
            conn = psycopg2.connect(connstr)

            # Abrir un cursor para realizar operaciones sobre la base de datos
            cur = conn.cursor()
            query_insert = "INSERT INTO hr_leave(id,holiday_status_id, date_from,date_to,name,state,payslip_status,user_id,employee_id,number_of_days,holiday_type,request_date_from,request_date_to,request_date_from_period,request_unit_half,request_unit_hours,request_unit_custom,create_uid,create_date,write_uid,write_date) VALUES ('7','2', '30/05/2019 08:00:00', '31/05/2019 17:00:00', 'eureka','confirm','False','2','1','2','employee','28/05/2019','29/05/2019','am', 'False','False','False','2','24/05/2019 15:58:55.23','2','24/05/2019 15:58:55.23');"
            cur.execute(query_insert)

            # Ejecutar una consulta SELECT
            # sqlquery = "select id, name from hr_leave;"
            # cur.execute(sqlquery)

            # Obtener los resultados como objetos Python
            # row = cur.fetchone()
            conn.commit()
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