from odoo import models, fields


class ResBank(models.Model):
    _inherit = 'res.bank'

    name = fields.Char(translate=True)
    mo_bank_id = fields.Many2one(comodel_name='res.bank')
    mo_correspondent_bank_ids = fields.One2many(
        comodel_name='res.bank',
        inverse_name='mo_bank_id',
        string='Correspondent bank',
        copy=True,
        auto_join=True)
    