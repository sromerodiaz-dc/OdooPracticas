from odoo import models, fields 

# "Por cada médico un modelo con nombre, apellidos y número de colegiado"
class Doctor(models.Model):
    _name = 'hospital.doctor'
    _description = 'Médico'

    name = fields.Char(string='Nombre', required=True)
    last_name = fields.Char(string='Apellidos', required=True)
    medical_license = fields.Char(string='Identificador único de cada doctor', required=True)

    # Cada doctor puede dar más de un diagnóstico, por eso One2many
    diagnosis_ids = fields.One2many(
        'hospital.diagnosis',
        'doctor_id',
        string='Diagnósticos'
    )
