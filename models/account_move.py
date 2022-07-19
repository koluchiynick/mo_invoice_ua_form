from odoo import models, fields

import logging


_logger = logging.getLogger(__name__)

try:
    from num2words import num2words
except ImportError:
    _logger.warning("The num2words python library is not installed, amount-to-text features won't be fully available.")
    num2words = None


class AccountMove(models.Model):
    _inherit = "account.move"
    
    def amount_to_ukr_text(self, amount):
        self.ensure_one()
        
        if num2words is None:
            logging.getLogger(__name__).warning("The library 'num2words' is missing, cannot render textual amounts.")
            return ""
        
        integer_value = int(amount)
        fractional_value = round(100 * (amount - integer_value))
        
        amount_words = '{} {} {:0>2} {}'.format(
            num2words(integer_value, lang='uk'),
            self.currency_id.mo_currency_unit_print_label,
            fractional_value,
            self.currency_id.mo_currency_subunit_print_label,
            ).capitalize()
        
        if self.amount_tax > 0:
            amount_words = amount_words + ' У т.ч. ПДВ: ' + '{} {}'.format(self.amount_tax, self.currency_id.mo_currency_unit_print_label)
        
        return amount_words
    