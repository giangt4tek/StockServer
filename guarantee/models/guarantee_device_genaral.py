from odoo import models, fields, api
import logging
_logger = logging.getLogger(__name__)

class GuaranteeDeviceGenaral(models.Model):
      _name = 'guarantee.device.genaral'
      
      product_id = fields.Many2one(
        'product.product', 
        string='Product', 
        required=True, 
        domain=[('type', '=', 'product'), ('tracking', '=', 'serial')]  )
      serial_tracking = fields.Char(string='Serial Tracking', required=True)

      user = fields.Many2one('res.users', string='User', required=True, default=lambda self: self.env.user)
      phone = fields.Char(
                 string='Chủ tài khoản',
                 related='user.phone',
                 store=True,
                 readonly=True)
      email = fields.Char(
                 string='Chủ tài khoản',
                 related='user.email',
                 store=True,
                 readonly=True)
     
      
      guarantee_period = fields.Integer(string='Guarantee period (months)', required=True)
      guarantee_start_date = fields.Date(string='Guarantee Start Date', required=True)
      guarantee_end_date = fields.Date(string='Guarantee End Date', required=True)
      
      guarantee_count = fields.Char(string='Guarantee count', required=True)
      details_ids = fields.One2many(
                  'guarantee.device.detail',
                  'general_id',
                  string="Guarantee Details")