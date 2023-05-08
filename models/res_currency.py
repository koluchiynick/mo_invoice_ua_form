from num2words import num2words

from odoo import models, fields, tools


class Currency(models.Model):
    _inherit = "res.currency"


    def amount_to_text(self, amount, lang_print='uk'):
        self.ensure_one()
        lang = tools.get_lang(self.env)
        
        if lang.iso_code == 'uk':
            if amount:
                return num2words(
                    tools.float_utils.float_round(
                        float(amount), precision_digits=self.decimal_places),
                    lang=lang_print,
                    to='currency',
                    cents=False,
                    currency=self.name,
                )
            else:
                return ''

        else:
            return super().amount_to_text(amount)

    def currency_name_to_ua(self):
        self.ensure_one()
        if self.name == 'EUR':
            return 'ЄВРО'
        if self.name == 'USD':
            return 'Долар США'
        return self.name
