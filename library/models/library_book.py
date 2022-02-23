from odoo import models, fields 

class LibraryBook(models.Model): 
    _name = 'library.book' 
    _description = 'manage library book'

    _sql_constraints = [
    ('name_uniq', # cons name
    'UNIQUE (name,publisher_id)', # cons
    'Book and Publisher must be unique.') #warning
    ]
    
    name = fields.Char('Title', required=True) 
    date_release = fields.Date('Release Date')
    date_borrowed = fields.Datetime('Borrowed Date')
    author_ids = fields.Many2many('res.partner',string='Authors')
    publisher_id = fields.Many2one('res.partner', string='Publisher')
    price_cn = fields.Integer('Price in CN') 
    price_au = fields.Integer('Price in AU', compute='_compute_au_price', inverse = '_inverse_au_price') 

    
    def name_get(self):
        result = []
        for record in self:
            rec_name = f"{record.name}-({record.date_release})"
            result.append((record.id, rec_name))
        return result
    
    def _compute_au_price(self):
        for book in self:
            if book.price_cn:
                book.price_au = book.price_cn / 5
            else:
                book.price_au = 0
    
    def _inverse_au_price(self):
        ...



class ResPartner(models.Model):
    _inherit = 'res.partner'
    published_book_ids = fields.One2many('library.book', 'publisher_id', string='Published Books')