from odoo import api, fields, models, _
from odoo.exceptions import UserError

class RentBookWiz (models.TransientModel):
    _name='rent.book.wiz'
    _description='rent book wiz'

    borrower_id = fields.Many2one('res.partner', string='Borrowed Person')
    book_ids = fields.Many2many('library.book', string='Books')

    def batch_rent_book(self):
        rentModel = self.env['library.book.rent']
        for wiz in self:
            for book in wiz.book_ids:
                rentModel.create({
                    'borrower_id':wiz.borrower_id.id,
                    'book_id': book.id
                })