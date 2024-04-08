from datetime import date
from odoo import api, fields, models


class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "HospitalPatient"

    name = fields.Char(string='Name', tracking=True)
    date_of_birth = fields.Date(string='Date Of Birth')
    ref = fields.Char(string='Reference')
    age = fields.Integer(string='AGE', compute='_compute_age', tracking=True)
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string='GENDER', tracking=True)
    active = fields.Boolean(string="Active", default=True)
    appointment_id = fields.Many2one('hospital.appointment', string='Appointments')
    image = fields.Image(string="Image")
    tag_ids = fields.Many2many('patient.tag', string="Tags")

    @api.depends('date_of_birth')
    def _compute_age(self):
        for rec in self:
            today = date.today()
            if rec.date_of_birth:
                rec.age = today.year - rec.date_of_birth.year
            else:
                rec.age = 0

    def name_get(self):
        patient_list = []
        for record in self:
            name = record.ref + '  ' + record.name
            patient_list.append((record.id, name))
        return patient_list
