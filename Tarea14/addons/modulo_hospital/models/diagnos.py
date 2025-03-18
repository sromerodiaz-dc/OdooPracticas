from odoo import models, fields

# Modelo del diagnostico dado del doctor al paciente
class Diagnosis(models.Model):
    _name = 'hospital.diagnosis'
    _description = 'Diagnóstico'
    _order = 'date desc'

    diagnosis = fields.Text(string='Diagnóstico', required=True)
    date = fields.Date(string='Fecha', default=fields.Date.today, required=True)

    # Cada registro de diagnostico se asocia con un unico doctor o paciente
    doctor_id = fields.Many2one(
        'hospital.doctor',
        string='Médico',
        required=True
    )

    # Los pacientes tambien ya que pueden tener diferentes diagnosticos a lo largo del tiempo
    patient_id = fields.Many2one(
        'hospital.patient',
        string='Paciente',
        required=True
    )