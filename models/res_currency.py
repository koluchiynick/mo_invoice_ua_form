from odoo import models, fields


class Currency(models.Model):
    _inherit = "res.currency"

    mo_currency_unit_print_label = fields.Char(
        string="Currency Unit print label",
        help="Currency Unit Print Name",
        translate=True)
    mo_currency_subunit_print_label = fields.Char(
        string="Currency Subunit print label",
        help="Currency Subunit Print Name",
        translate=True)
