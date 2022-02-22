from odoo import models, fields 

class LibraryBook(models.Model): 
    _name = 'library.book' 
    _description = 'manage library book'
    
    name = fields.Char('Title', required=True) 
    date_release = fields.Date('Release Date')
    date_borrowed = fields.Datetime('Borrowed Date')
    author_ids = fields.Many2many('res.partner',string='Authors')
    publisher_id = fields.Many2one('res.partner', string='Publisher')
    