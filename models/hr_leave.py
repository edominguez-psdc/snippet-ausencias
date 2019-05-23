from odoo import api, fields, models


class HolidaysRequest(models.Model):
    _inherit = 'hr.leave'

    def website_form_input(self, request, values):
        pass