"""import psycopg2
from odoo import http
from odoo.http import request"""


"""class WebsiteFormAu(WebsiteFormAu):

    @http.route('/website_form/<string:model_name>', type='http', auth="public", methods=['POST'], website=True)
    def connectionBD(self):
        import psycopg2
        
        connection = psycopg2.connect(user="test", password="12345", host="127.0.0.1", port="5432", database="leave12")

        connection = psycopg2.connect(user="test",
                                        password="12345",
                                        host="127.0.0.1",
                                        port="5432",
                                        database="leave12")
        cursor= connection.cursor()

        query_insert = "INSERT INTO hr_leave(id,holiday_status_id, date_from,date_to,name,state,payslip_status,user_id,employee_id,number_of_days,holiday_type,request_date_from,request_date_to,request_date_from_period,request_unit_half,request_unit_hours,request_unit_custom,create_uid,create_date,write_uid,write_date) VALUES ('7','2', '30/05/2019 08:00:00', '31/05/2019 17:00:00', 'eureka','confirm','False','2','1','2','employee','28/05/2019','29/05/2019','am', 'False','False','False','2','24/05/2019 15:58:55.23','2','24/05/2019 15:58:55.23');"

        cursor.execute(query_insert)
        connection.commit()
        cursor.close()
        connection.close()"""



""" Forma correcta - aun sin saber como

# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
from odoo.addons.website_form.controllers.main import WebsiteForm

 
class WebsiteForm(WebsiteForm):

    # Check and insert values from the form on the model <model>
    @http.route('/website_form/<string:model_name>', type='http', auth="public", methods=['POST'], website=True)
    def website_form_input(self, model_name, **kwargs):
        if model_name == 'hr.leave' and not request.params.get('state_id'):
            geoip_country_code = request.session.get('geoip', {}).get('country_code')
            geoip_state_code = request.session.get('geoip', {}).get('region')
            if geoip_country_code and geoip_state_code:
                State = request.env['res.country.state']
                request.params['state_id'] = State.search([('code', '=', geoip_state_code), ('country_id.code', '=', geoip_country_code)]).id

        return super(WebsiteForm, self).website_form(model_name, **kwargs)

    def insert_record(self, request, model, values, custom, meta=None):
        if model.model == 'crm.lead':
            if 'company_id' not in values:
                values['company_id'] = request.website.company_id.id
        return super(WebsiteForm, self).insert_record(request, model, values, custom, meta=meta)
"""
