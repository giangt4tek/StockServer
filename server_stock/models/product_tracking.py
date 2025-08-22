from odoo import models, fields, api
import logging
_logger = logging.getLogger(__name__)

class ProductTracking(models.Model):
      _inherit = 'product.template'
      

      tracking = fields.Selection(
        selection=[('serial', 'By Unique Serial Number')],
        string="Tracking",
        default='serial',
        required=True
    )