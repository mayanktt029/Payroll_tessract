from odoo import models, fields, api
from odoo.exceptions import ValidationError
import re
from datetime import date
from dateutil.relativedelta import relativedelta

class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    pf_account_no = fields.Char(string="PF Account No.", size=26, help="Enter PF Account No. in the format 'AA/AAA/0000000/000/0000000'")
    uan_no = fields.Char(string="UAN No.", size=12, help="Enter UAN No. (Numeric, 12 digits only)")
    date_of_joining = fields.Date(string="Date of Joining", default=fields.Date.today, help="The date the employee joined the company")
    days_since_joining = fields.Char(string="Time Since Joining", compute="_compute_days_since_joining", store=True)
    termination_date = fields.Date(string="Termination Date", help="The date the employee left the company")



    @api.constrains('pf_account_no')
    def _check_pf_account_no(self):
        for record in self:
            if record.pf_account_no:
                # Updated regular expression for the format 'AA/AAA/0000000/000/0000000'
                pf_regex = r'^[A-Za-z]{2}/[A-Za-z]{3}/\d{7}/\d{3}/\d{7}$'
                if not re.match(pf_regex, record.pf_account_no):
                    raise ValidationError("PF Account No. must follow the format 'AA/AAA/0000000/000/0000000'.")

    @api.constrains('uan_no')
    def _check_uan_no(self):
        for record in self:
            if record.uan_no:
                if not re.match(r'^\d{12}$', record.uan_no):
                    raise ValidationError("UAN No. must be 12 digits and numeric.")

    @api.constrains('date_of_joining')
    def _check_date_of_joining(self):
        for record in self:
            if record.date_of_joining and record.date_of_joining > date.today():
                raise ValidationError("Date of Joining cannot be set to a future date.")

    @api.depends('date_of_joining')
    def _compute_days_since_joining(self):
        for record in self:
            if record.date_of_joining:
                delta = relativedelta(date.today(), record.date_of_joining)
                years = delta.years
                months = delta.months
                days = delta.days
                record.days_since_joining = f"{years} year, {months} month, {days} day"
            else:
                record.days_since_joining = "0 year, 0 month, 0 day"
