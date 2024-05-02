# --*-- coding: utf8 --*--

from odoo import fields, _ , models, api
from odoo.exceptions import ValidationError

class RetenuSourceLine(models.Model):
    _name="retenue.source.line"
    _descripiton="ligne(s) de retenue à la source"
    _rec_name = "account_invoice_id"

    account_invoice_id = fields.Many2one(
        'account.invoice',
        string='Facture',
    )

    move_id = fields.Many2one(
        'retenue.source',
    )

    # ================ field for compute tva ===============
    tva_recu = fields.Integer(
        string='Tva recu',
    )

    tva_aj = fields.Integer(
        string="Tva ajust"
    )
    
    tva_esp = fields.Integer(
        string="Tva esp",
        compute="_get_default_values",
        store=True,
    )

    # ================== field for a/ir ===================

    ir_recu = fields.Integer(
        string='A/IR recu',
    )

    ir_aj = fields.Integer(
        string="A/IR ajust"
    )

    ir_esp = fields.Integer(
        string="A/IR esp",
        compute="_get_default_values",
        help='accoumpt et Impot sur revenur 2,2%'
    )

    date = fields.Date(
        string="Date",
        compute="_get_default_values",
        store=True,
    )

    invoice_ttc = fields.Integer(
        string="Mnt TTC",
        compute="_get_default_values",
        store=True,
    )

    invoice_ht = fields.Integer(
        string="Mnt HT",
        compute="_get_default_values",
        store=True
    )

    @api.onchange('account_invoice_id')
    def _onchange_account_invoice_id(self):
        for record in self:
            if not record.account_invoice_id:
                table = []
                model = self.env['account.invoice'].search([
                    ('partner_id', '=', record.move_id.partner_id.id), ('state', '=', 'open' )
                ])
                for data in model:
                    table.append(data.id)

                return {'domain': {'account_invoice_id': [('id', 'in', table), ]}}
                
            elif not record.move_id.partner_id:
                raise ValidationError('Remplir le partenaire au préalable')

    @api.depends('account_invoice_id')
    def _get_default_values(self):
        for record in self:
            if record.account_invoice_id:
                total = (record.account_invoice_id.amount_untaxed * 2.2)/100
                record.ir_esp = total
                record.date = record.account_invoice_id.date_invoice
                record.invoice_ttc = record.account_invoice_id.amount_total
                record.invoice_ht = record.account_invoice_id.amount_untaxed
                record.tva_esp = record.account_invoice_id.amount_tax_signed


    @api.onchange('tva_recu')
    def _compute_tva_ajustement(self):
        for record in self:
            if record.tva_recu:
                tva_aj = record.tva_esp - record.tva_recu
                if abs(tva_aj) > 100:
                    raise ValidationError("L'ajustement TVA ne doit être supérieur à 100 FCFA")
                else: 
                   record.tva_aj = record.tva_esp - record.tva_recu 

    
    @api.onchange('ir_recu')
    def _compute_ir_ajustement(self):
        for record in self:
            if record.tva_recu:
                ir_aj = record.ir_esp - record.ir_recu
                if abs(ir_aj) > 100:
                    raise ValidationError("L'ajustement A/IRne doit être supérieur à 100 FCFA")
                else:
                    record.ir_aj = record.ir_esp - record.ir_recu   