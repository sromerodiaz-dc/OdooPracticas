# tarea 15
Para realizar la tarea el enunciado dice que los modelos han de ser los siguientes:
Paciente: hospital.patient
Médico: hospital.doctor
Diagnóstico: hospital.diagnosis

Según lo que dice el enunciado las relaciones:

Un médico puede tener múltiples diagnósticos (One2many).
Un paciente puede tener múltiples diagnósticos (One2many).
Cada diagnóstico vincula un médico y un paciente (Many2one).

Las vistas han de ser tree,form y kanban para los 3 modelos.

Y hay que meter datos de demo.

## Desarrollo

### `Manifiesto`
El manifest es... y es importante por...
```t
# -*- coding: utf-8 -*-
{
    'name': "hospital",

    'summary': "Manejo Hospital",

    'description': """
Manejo de pacientes, doctores y sus respectivos diagnosticos
    """,

    'author': "Santiago Romero",
    'website': "danielcastelao.org",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
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
Se indica a Odoo de donde cargar los datos que se piden como los datos de demostración y las diferentes views.

### `Modelos`
Los modelos tienen que ser tres y se encapsulan en los archivos diagnos.py, doctor.py y patient.py

```python
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
```

Luego los archivos de paciente y doctor son más cortos:
```python
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
```

```python
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
```

### `Archivo CSV: ACLs`
// explicacion de por que es importante hacer el archivo y como funciona el formato del mismo
```
id,name,model_id:id,group_id:id,perm_read,perm_write,perm_create,perm_unlink
access_hospital_diagnosis,access_hospital_diagnosis,model_hospital_diagnosis,base.group_user,1,1,1,1
access_hospital_doctor,access_hospital_doctor,model_hospital_doctor,base.group_user,1,1,1,1
access_hospital_patient,access_hospital_patient,model_hospital_patient,base.group_user,1,1,1,1
```

### `Vistas: FORM, TREE y KANBAN`
// Explicar el formato de las vistas, como se ve cada una y tambien explicar los actions y los menus. Para estos ultimos tambien explicar la sintaxis.

Ejemplo empleado en el ejercicio de FORM:
```
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

Ejemplo de TREE:
```
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

Ejemplo de KANBAN:
```
<record model="ir.ui.view" id="view_patient_kanban">
    <field name="name">hospital.patient.kanban</field>
    <field name="model">hospital.patient</field>
    <field name="arch" type="xml">
        <kanban>
            <field name="name"/>
            <field name="symptoms"/>
            <templates>
                <t t-name="kanban-box">
                    <div class="oe_kanban_global_click">
                        <div class="o_kanban_record_title">
                            <strong><field name="name"/></strong>
                            <br/>
                            <span><field name="last_name"/></span>
                        </div>
                        <div class="o_kanban_record_body">
                            <span><field name="symptoms"/></span>
                        </div>
                    </div>
                </t>
            </templates>
        </kanban>
    </field>
</record>
```

Ejemplo de los menus usados:
```
<!-- Menús -->
<menuitem 
    id="menu_hospital_root" 
    name="Hospital" 
    sequence="10"
    groups="base.group_user"
/>

<menuitem id="menu_hospital_patients" name="Pacientes" parent="menu_hospital_root" action="action_patients"/>
<menuitem id="menu_hospital_doctors" name="Médicos" parent="menu_hospital_root" action="action_doctors"/>
<menuitem id="menu_hospital_diagnoses" name="Diagnósticos" parent="menu_hospital_root" action="action_diagnoses"/>
```

Ejemplo de los "actions" empleados por los menus:
```
<record model="ir.actions.act_window" id="action_patients">
    <field name="name">Pacientes</field>
    <field name="res_model">hospital.patient</field>
    <field name="view_mode">tree,form,kanban</field>
</record>

<record model="ir.actions.act_window" id="action_doctors">
    <field name="name">Médicos</field>
    <field name="res_model">hospital.doctor</field>
    <field name="view_mode">tree,form</field>
</record>

<record model="ir.actions.act_window" id="action_diagnoses">
    <field name="name">Diagnósticos</field>
    <field name="res_model">hospital.diagnosis</field>
    <field name="view_mode">tree,form</field>
</record>
```