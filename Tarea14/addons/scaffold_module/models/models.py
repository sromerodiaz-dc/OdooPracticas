# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import date

class partner_zodiac(models.Model):
    # funciona "como un import"
    _inherit = 'res.partner'

    f_nac = fields.Date("Fecha de nacimiento")
    # NO SE DEBE ALMACENAR LA EDAD EN LA BD, ES MALA PRÁXIS, PERO LO HACEMOS CON FINES DE APRENDIZAJE
    edad = fields.Integer(string="Edad", readonly=True, compute="_calcular_edad", store=True)
    signo_zodiacal = fields.Char(string="Signo zodiacal", readonly=True, compute="_calcular_signo", store=True)

    # Extensión funcionalidad tarea 14
    linkedin_profile = fields.Char(string="Perfil de LinkedIn")
    is_social_active = fields.Boolean(string="Activo en redes sociales", compute="_isActive", store = True)

    @api.depends('f_nac')
    def _calcular_edad(self):
        for record in self:
            # nos aseguramos que existe la fecha de nacimiento
            if record.f_nac:
                # resta el año actual con el año de nacimiento
                today = date.today()
                edad = today.year - record.f_nac.year
                record.edad = edad

    @api.depends('f_nac')
    def _calcular_signo(self):
        for record in self:
            try:
                # nos aseguramos que existe la fecha de nacimiento
                if record.f_nac:
                    # inserta aquí el código para calcular el signo
                    day = record.f_nac.day
                    month = record.f_nac.month

                    # estructura If-Elif hecho con chatgpt
                    if (month == 1 and day >= 20) or (month == 2 and day <= 18):
                        record.signo_zodiacal = "Acuario"
                    elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
                        record.signo_zodiacal = "Piscis"
                    elif (month == 3 and day >= 21) or (month == 4 and day <= 19):
                        record.signo_zodiacal = "Aries"
                    elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
                        record.signo_zodiacal = "Tauro"
                    elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
                        record.signo_zodiacal = "Géminis"
                    elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
                        record.signo_zodiacal = "Cáncer"
                    elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
                        record.signo_zodiacal = "Leo"
                    elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
                        record.signo_zodiacal = "Virgo"
                    elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
                        record.signo_zodiacal = "Libra"
                    elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
                        record.signo_zodiacal = "Escorpio"
                    elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
                        record.signo_zodiacal = "Sagitario"
                    else:
                        record.signo_zodiacal = "Capricornio"
            except Exception:
                record.signo_zodiacal = "Sin signo"

    # Extensión de funcionalidad tarea 14
    @api.depends('linkedin_profile')
    def _isActive(self):
        for record in self:
            record.is_social_active = bool(record.linkedin_profile)