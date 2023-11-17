from odoo import models, fields


class LibraryBookCategory(models.Model):
    _name = 'library.book.category'
    _description = 'Library book category'

    name = fields.Char(
        required=True,
    )
