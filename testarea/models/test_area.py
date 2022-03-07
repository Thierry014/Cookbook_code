from email.mime import base
from odoo import models, fields, api,_
import logging

_logger = logging.getLogger(__name__)
# _logger.error("Error when creating COA %s", coa.name, exc_info=True)


class TestArea(models.Model): 
    _name = 'test.area' 
    _description = '' 

    name = fields.Char()
    base_number = fields.Integer()
    numbers = fields.Integer(compute='change_num')

    def test_fun(self):
        print('>>>>>>>>>>>>>>>>')

    @api.onchange('name')
    def change_name(self):
         _logger.warning(_(f"Name change to {self.name}"))

    @api.depends('base_number')
    def change_num(self):
        for r in self:
            _logger.warning(_(f"base number changed"))
            if r.base_number:
                r.numbers = r.base_number * 2
            else:
                r.numbers = 1
        # self.numbers = 1
