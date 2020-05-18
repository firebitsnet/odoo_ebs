from odoo import fields, models, api


class Test (models.Model):
    _name = 'ebs.test'
    _description = 'EBS test'

    name = fields.Char()
    


