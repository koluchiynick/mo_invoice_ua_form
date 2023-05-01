from odoo import models, fields


class Partner(models.Model):
    _inherit = "res.partner"

    mo_full_name = fields.Char('Full name', translate=True)
    mo_edrpou = fields.Char(
        'EDRPOU',
        size=12,
    )
    mo_income_tax_payer = fields.Boolean('Income Tax Payer')
    mo_document_signer = fields.Many2one(comodel_name='res.partner',
                                         string='Document signer')
