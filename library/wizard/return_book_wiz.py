from odoo import api, fields, models, _
from odoo.exceptions import UserError

class ReturnBookWiz (models.TransientModel):
    _name='return.book.wiz'
    _description='return book wiz'

    borrower_id = fields.Many2one('res.partner', string='Borrowed Person')
    book_ids = fields.Many2many('library.book', string='Books')


    @api.onchange('borrower_id')
    def get_books(self):
        self.book_ids = self.env['library.book.rent'].search([('state', '=', 'ongoing'), ('borrower_id','=',self.borrower_id.id)]).mapped('book_id')
        # compare always use id 
        # map return list (non relationed field) or recordset (relation field)
    def batch_return_book(self):
        ...
