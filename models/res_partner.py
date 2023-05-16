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
    mo_main_bank_account_id = fields.Many2one(
        comodel_name='res.partner.bank',
        string="Main bank account",
        domain="[('partner_id', '=', id)]",
        help="Bank account number to which the invoice will be paid by default"
    )
    street = fields.Char(translate=True)
    city = fields.Char(translate=True)

    def adress_for_invoce_ua(self):
        return self._display_address(without_company=True)
