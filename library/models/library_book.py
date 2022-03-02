from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError


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
    price_au = fields.Integer('Price in AU', compute='_compute_au_price', inverse = '_inverse_au_price', default=123) 

    owner1 = fields.Many2one('res.partner', string="Owner with email", domain=[('email','!=',False)])
    owner2 = fields.Many2one('res.partner', string="Owner without mobile", domain=[('mobile','!=',False)] )

    state = fields.Selection([('onhand','On Hand'),('borrowed','Borrowed'),('lost','Lost')], default='onhand')
    book_is_ava = fields.Boolean('Book available', default = True)

    def name_get(self):
        result = []
        for record in self:
            rec_name = f"{record.name}-({record.date_release})"
            result.append((record.id, rec_name))
        return result
    
    @api.depends('price_cn')
    def _compute_au_price(self):
        for book in self:
            if book.price_cn:
                book.price_au = book.price_cn / 5
            else:
                book.price_au = 0
    
    def _inverse_au_price(self):
        ...

    def change_state(self):
        if self.state == 'borrowed':
            self.state = 'onhand'
        else:
            self.state = 'borrowed'


    def read_group_test(self):
        result = self.read_group([('price_cn', '!=', False)],['publisher_id'],['publisher_id'])
        print(f'>>>{result}')

    def make_borrowed(self):
        self.state = 'borrowed'

    def make_available(self):
        self.state = 'onhand'

    def rent_out(self):
        if self.state != 'onhand':
            raise UserError('Book is not available to rent')
        
        # create rent record
        rent_as_superuser = self.env['library.book.rent'].sudo()
        rent_as_superuser.create({
            'book_id': self.id,
            'borrower_id': self.env.user.partner_id.id,
        })

    def make_lost(self):
        if self.env.context.get('have_ctx'):
            print(f'>>>>>>>Make it lost{self.env.context}')
            self.state = 'lost'
        else:
            print(f">>>>>Can't make it lost {self.env.context}")
            raise UserError('No lost')

class ResPartner(models.Model):
    _inherit = 'res.partner'
    published_book_ids = fields.One2many('library.book', 'publisher_id', string='Published Books')