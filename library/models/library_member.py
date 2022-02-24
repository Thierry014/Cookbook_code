from odoo import models, fields 

class LibraryBook(models.Model): 
    _inherit = 'library.book'

    def change_state(self):
        res = super().change_state()
        self.book_is_ava = not self.book_is_ava
        print(f'>>>>>>>>>>{self.state}')
        return res