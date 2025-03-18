from odoo import models, fields

# "Por cada paciente un modelo con nombre, apellidos y sus respectivos síntomas"
class Patient(models.Model):
    _name = 'hospital.patient'
    _description = 'Paciente'

    name = fields.Char(string='Nombre', required=True)
    last_name = fields.Char(string='Apellidos', required=True)
    symptoms = fields.Text(string='Síntomas')

    # Un paciente puede tener múltiples diagnósticos por eso One2many
    diagnosis_ids = fields.One2many(
        'hospital.diagnosis',  # Modelo relacionado
        'patient_id',          # Campo inverso en diagnosis
        string='Historial de diagnósticos'
    )
