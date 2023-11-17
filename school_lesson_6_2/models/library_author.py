from odoo import fields, models, api


class LibraryAuthor(models.Model):
    _name = 'library.author'
    _description = 'Library Book Authors'

    first_name = fields.Char(
        required=True,
        translate=True,
    )
    last_name = fields.Char(
        required=True,
        translate=True,
    )
    birth_date = fields.Date('Birthday')
    create_time = fields.Float(
        string='Create time in seconds',
        compute='_compute_create_time',
    )

    def name_get(self):
        return [(rec.id, "%s %s" % (
            rec.first_name, rec.last_name)) for rec in self]

    @api.depends('create_date')
    def _compute_create_time(self):
        for book in self:
            book.create_time = book.create_date.timestamp()

    def action_delete(self):
        self.ensure_one()
        self.check_access_rights('unlink')
        self.unlink()

    def _create_by_user(self, vals):
        return self.sudo().create(vals)
