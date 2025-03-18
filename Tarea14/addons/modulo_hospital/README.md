# Tarea 15: Módulo Hospital en Odoo

En este `readme` detallo el desarrollo del módulo **Hospital** en Odoo, que maneja pacientes, médicos y diagnósticos.

## **Modelos y Relaciones**

### **Entidades del Módulo**
- **Paciente:** `hospital.patient`
- **Médico:** `hospital.doctor`
- **Diagnóstico:** `hospital.diagnosis`

### **Relaciones entre Modelos**
- Un **médico** puede tener múltiples diagnósticos (*One2many*).
- Un **paciente** puede tener múltiples diagnósticos (*One2many*).
- Cada **diagnóstico** vincula un médico y un paciente (***Many2one***).

## **Manifiesto del Módulo**

El **manifest** (`__manifest__.py`) informa a Odoo sobre la configuración del módulo:

```python
# -*- coding: utf-8 -*-
{
    'name': "hospital",
    'summary': "Manejo Hospital",
    'description': """
Manejo de pacientes, doctores y sus respectivos diagnósticos.
    """,
    'author': "Santiago Romero",
    'website': "danielcastelao.org",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
}
```

## **Definición de Modelos**

Cada modelo se define en su respectivo archivo:

### **Modelo `hospital.diagnosis`**
```python
from odoo import models, fields

class Diagnosis(models.Model):
    _name = 'hospital.diagnosis'
    _description = 'Diagnóstico'
    _order = 'date desc'

    diagnosis = fields.Text(string='Diagnóstico', required=True)
    date = fields.Date(string='Fecha', default=fields.Date.today, required=True)
    doctor_id = fields.Many2one('hospital.doctor', string='Médico', required=True)
    patient_id = fields.Many2one('hospital.patient', string='Paciente', required=True)
```

### **Modelo `hospital.doctor`**
```python
from odoo import models, fields

class Doctor(models.Model):
    _name = 'hospital.doctor'
    _description = 'Médico'

    name = fields.Char(string='Nombre', required=True)
    last_name = fields.Char(string='Apellidos', required=True)
    medical_license = fields.Char(string='Número de Colegiado', required=True)
    diagnosis_ids = fields.One2many('hospital.diagnosis', 'doctor_id', string='Diagnósticos')
```

### **Modelo `hospital.patient`**
```python
from odoo import models, fields

class Patient(models.Model):
    _name = 'hospital.patient'
    _description = 'Paciente'

    name = fields.Char(string='Nombre', required=True)
    last_name = fields.Char(string='Apellidos', required=True)
    symptoms = fields.Text(string='Síntomas')
    diagnosis_ids = fields.One2many('hospital.diagnosis', 'patient_id', string='Historial de diagnósticos')
```

## **Archivo CSV: ACLs (Permisos de Acceso)**

El archivo `ir.model.access.csv` define los permisos para cada modelo:

```csv
id,name,model_id:id,group_id:id,perm_read,perm_write,perm_create,perm_unlink
access_hospital_diagnosis,access_hospital_diagnosis,model_hospital_diagnosis,base.group_user,1,1,1,1
access_hospital_doctor,access_hospital_doctor,model_hospital_doctor,base.group_user,1,1,1,1
access_hospital_patient,access_hospital_patient,model_hospital_patient,base.group_user,1,1,1,1
```

## **Vistas: FORM y TREE**

Odoo utiliza XML para definir las vistas. A continuación, se presentan ejemplos de cada tipo.

### **Vista FORM para Pacientes**
```xml
<record model="ir.ui.view" id="view_patient_form">
    <field name="name">hospital.patient.form</field>
    <field name="model">hospital.patient</field>
    <field name="arch" type="xml">
        <form>
            <sheet>
                <group>
                    <field name="name" string="Nombre"/>
                    <field name="last_name" string="Apellidos"/>
                    <field name="symptoms" string="Síntomas"/>
                </group>
                <notebook>
                    <page string="Diagnósticos">
                        <field name="diagnosis_ids" mode="tree, form">
                            <tree>
                                <field name="date" string="Fecha"/>
                                <field name="doctor_id" string="Médico"/>
                                <field name="diagnosis" string="Diagnóstico"/>
                            </tree>
                        </field>
                    </page>
                </notebook>
            </sheet>
        </form>
    </field>
</record>
```

### **Vista TREE para Pacientes**
```xml
<record model="ir.ui.view" id="view_patient_tree">
    <field name="name">hospital.patient.tree</field>
    <field name="model">hospital.patient</field>
    <field name="arch" type="xml">
        <tree>
            <field name="name" string="Nombre"/>
            <field name="last_name" string="Apellidos"/>
            <field name="symptoms" string="Síntomas"/>
        </tree>
    </field>
</record>
```

## **Menús y Acciones**

### **Menús**
```xml
<menuitem id="menu_hospital_root" name="Hospital" sequence="10" groups="base.group_user"/>
<menuitem id="menu_hospital_patients" name="Pacientes" parent="menu_hospital_root" action="action_patients"/>
<menuitem id="menu_hospital_doctors" name="Médicos" parent="menu_hospital_root" action="action_doctors"/>
<menuitem id="menu_hospital_diagnoses" name="Diagnósticos" parent="menu_hospital_root" action="action_diagnoses"/>
```

### **Acciones**
```xml
<record model="ir.actions.act_window" id="action_patients">
    <field name="name">Pacientes</field>
    <field name="res_model">hospital.patient</field>
    <field name="view_mode">tree,form,kanban</field>
</record>
```

---

