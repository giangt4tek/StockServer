from odoo import models, fields, api
import logging
_logger = logging.getLogger(__name__)

class GuaranteeDevice(models.Model):
      _name = 'guarantee.genaral.detail'
      
      guarantee_general_id = fields.Many2one('guarantee.device.genaral', string='Guarantee General', required=True)
      
      guarantee_reason = fields.Text(string='Reason', required=False)
      guarantee_loacation = fields.Char(string='Guarantee location', required=True)

      receive_date = fields.Date(string='Receive date', required=False)
      repair = fields.Text(string='repair', required=False)
      repair_time = fields.Date(string='Repair time', required=False)
      repair_done = fields.Boolean(string='Repair done', default=False)
      handover_date = fields.Date(string='Handover date', required=False)

      note = fields.Text(string='Note', required=False)
