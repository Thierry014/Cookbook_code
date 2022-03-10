from odoo import models, fields 

SEL =[('a','A'),('b','B'),('c','C'),('d','D')]

class HenryView(models.Model): 
    _name = 'henry.view' 
    _description = 'view template' 

    name = fields.Char("Name")
    view_text = fields.Text("Text")
    view_number = fields.Integer("Number")
    view_bool = fields.Boolean('Boolean')
    view_sel = fields.Selection(SEL)

    def bnv_in_view(self):
        ...