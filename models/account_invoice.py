 # --*-- coding:utf8 --*--

from odoo import models, fields, api, _
from odoo.osv import expression
import json
from odoo.tools import email_re, email_split, email_escape_char, float_is_zero, float_compare, \
    pycompat, date_utils

class CustomAccountInvoice(models.Model):
    _inherit="account.invoice"

    retenue_source_id = fields.Many2one(
        'retenue.source'
    )

    @api.model
    def _name_search(self, name, args=None, operator='ilike', limit=100, name_get_uid=None):
        args = args or []
        domain = []
        if name:
            domain = [('number', operator, name)]
        account_invoice_ids = self._search(expression.AND([domain, args]), limit=limit, access_rights_uid=name_get_uid)
        return self.browse(account_invoice_ids).name_get()

    @api.one
    @api.depends('payment_move_line_ids.amount_residual')
    def _get_payment_info_JSON(self):
        self.payments_widget = json.dumps(False)
        if self.payment_move_line_ids:
            info = {'title': _('Less Payment'), 'outstanding': False, 'content': self._get_payments_vals()}
            self.payments_widget = json.dumps(info, default=date_utils.json_default)

   

class CustomAccountMove(models.Model):
    _inherit="account.move"

    retenu_source_id = fields.Many2one(
        'retenu.source'
    )

    # has_retenu = fields.Boolean(
    #     string="A une Retenu",
    #     compute="_get_value",
    #     store=True,
    # )

    def _get_value(self):
        for record in self:
            if record.retenu_source_id:
                record.has_retenu = True

    invoice_id = fields.Many2one(
        'account.invoice'
    )


class CustomAccountInvoiceTax(models.Model):
    _inherit="account.invoice.tax"

    retenu_source_id = fields.Many2one(
        'retenu.source'
    )


class CustomAccountMoveLine(models.Model):
    _inherit = "account.move.line"

    @api.constrains('debit', 'credit')
    def _check_debit_credit_null(self):
        for line in self:
            if line.debit is 0 and line.credit is 0:
                line.unlink()