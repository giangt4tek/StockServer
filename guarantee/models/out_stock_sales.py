from odoo import models, fields, api
import logging
_logger = logging.getLogger(__name__)

class sell(models.Model):
    _inherit = 'account.move'