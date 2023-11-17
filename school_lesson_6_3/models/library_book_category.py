from odoo import models, fields, api, _


class LibraryBookCategory(models.Model):
    _name = 'library.book.category'
    _description = 'Library book category'

    name = fields.Char(
        required=True,
    )
    book_ids = fields.One2many(
        string='Books',
        comodel_name='library.book',
        inverse_name='category_id',
    )
    book_total = fields.Integer(
        string='Book count',
        compute='_compute_book_total',
    )

    @api.depends('book_ids')
    def _compute_book_total(self):
        """Compute book_total field as count books of category."""
        for category in self:
            category.book_total = len(category.book_ids)

    def action_open_books(self):
        """Open tree,form views when button 'Books' clicked."""
        self.ensure_one()
        return {
            'name': _('Books'),
            'type': 'ir.actions.act_window',
            'view_mode': 'tree,form',
            'res_model': 'library.book',
            'domain': [('id', 'in', self.book_ids.ids)],
            'target': 'current',
        }
