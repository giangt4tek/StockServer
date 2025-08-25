from odoo import models, fields, api
import logging
_logger = logging.getLogger(__name__)

class GuaranteeDevice(models.Model):
      _inherit = 'guarantee.device'
      
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
      guarantee_reason = fields.Text(string='Reason', required=False)
      guarantee_loacation = fields.Char(string='Guarantee location', required=True)

      receive_date = fields.Date(string='Receive date', required=False)
      repair = fields.Text(string='repair', required=False)
      repair_time = fields.Date(string='Repair time', required=False)
      repair_done = fields.Boolean(string='Repair done', default=False)
      handover_date = fields.Date(string='Handover date', required=False)

      note = fields.Text(string='Note', required=False)
