from odoo import models, fields


class ResCompany(models.Model):
    _inherit = 'res.company'

    sign_image = fields.Image(string="Facsimile signature")
    stamp_image = fields.Image(string="Stamp of company")
