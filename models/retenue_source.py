# --*-- coding:utf8 --*--

from odoo import fields, models, api, _
from datetime import date as Date

import logging 
_logger = logging.getLogger(__name__)

class RetenueSource(models.Model):
    _name="retenue.source"
    _inherit=['mail.thread', 'mail.activity.mixin']
    _description="Gestion des returnu à la source"
    _rec_name="name"

    state = fields.Selection(
        [
            ('draft', 'Bourillon'),
            ('to_approuv', 'A approuver'),
            ('valide', 'Validé')
        ],
        default='draft',
        index=True,
        string="Status",
        track_visibility="onchange"
    )

    line_ids = fields.One2many(
        'retenue.source.line',
        'move_id',
    )

    name = fields.Char(
        string="Name"
    )

    partner_id = fields.Many2one(
        'res.partner',
        string="partenaire",
        track_visibility="onchange",
    )

    date = fields.Date(
        string="Date Comptable",
        default=Date.today()
    )

    date_piece = fields.Date(
        string="Date Pièce"
    )

    reference = fields.Char(
        string="Reference"
    )
    
    journal_id = fields.Many2one(
        'account.journal',
        default=lambda self: self.env['account.journal'].search(
            [('name', '=', 'ODS')], limit=1),
        string='Journal', 
    )

    company_id = fields.Many2one(
        'res.company',
        string=_('Company'),
        default = lambda self: self.env.user.company_id,
        change_default=True,
    )

    montant_total = fields.Integer(
        string="Montant Total",
        compute="_comute_amount_total",
    )

    currency_id = fields.Many2one(
        'res.currency', 
        compute='_compute_currency',
        store=True,
        oldname='currency', 
        string="Currency"
    )

    @api.model
    def create(self, values):
        if values.get('name', _('New')) == _('New'):
            # Get the company from the values or use the current user's company
            company_id = values.get('company_id') or self.env.user.company_id.id
            # Get the sequence based on the company
            sequence = self.env['ir.sequence'].with_context(force_company=company_id).next_by_code('retenue.source') or _('New')
            values['name'] = sequence
        result = super(RetenueSource, self).create(values)
        return result

    @api.depends('name')
    def name_get(self):
        res = []
        for record in self:
            res.append((record.id, ("%s") % (record.name)))

        return res

 
    @api.multi
    def action_validate(self):
        
        account_ir_id  = self.env['account.account'].search(
            [
                ('code', '=', '449211')
            ], limit=1
        ).id

        account_tva_id = self.env['account.account'].search(
            [
                ('code', '=', '444101')
            ], limit=1
        ).id

        account_partner_id = self.env['account.account'].search(
            [
                ('code', '=', '411100')
            ], limit=1
        ).id

        if self.state == "to_approuv":    
            data =  list()
            for record in self:
                for data_line in record.line_ids:
                    if data_line.tva_aj == 0 and data_line.ir_aj == 0:
                         data.append({
                        'date': record.date,
                        'date_fat': record.date_piece,
                        'journal_id': record.journal_id.id,
                        'company_id': record.company_id.id,
                        'ref': record.reference,
                        'invoice_id': data_line.account_invoice_id.id,
                        'retenu_source_id': record.id,
                        'line_ids': [(0, 0,
                                {   # ++==++  TVA ++==++
                                    'account_id': account_tva_id,
                                    'partner_id': record.partner_id.id,
                                    'name': record.reference,
                                    'no_facture': data_line.account_invoice_id.number.split('/')[-1],
                                    'date_facture': record.date_piece,
                                    'ref_facture': record.reference,
                                    'debit': data_line.tva_recu,
                                }),
                                (0, 0, {   # ++==++ A/IR ++==++
                                    'account_id': account_ir_id,
                                    'partner_id': record.partner_id.id,
                                    'name': record.reference,
                                    'no_facture': data_line.account_invoice_id.number.split('/')[-1],
                                    'date_facture': record.date_piece,
                                    'ref_facture': record.reference,
                                    'debit': data_line.ir_recu,
                                    'credit': 0
                                }),
                                (0, 0, {   # ++==++ Compte du tiers ++==++
                                    'account_id': account_partner_id,
                                    'partner_id': record.partner_id.id,
                                    'name': record.reference,
                                    'no_facture': data_line.account_invoice_id.number.split('/')[-1] ,
                                    'date_facture': record.date_piece,
                                    'ref_facture': record.reference,
                                    "credit": sum([data_line.tva_recu, data_line.tva_aj, data_line.ir_recu, data_line.ir_aj])
                                })

                            ]
                    })


                    elif data_line.tva_aj != 0 and data_line.ir_aj == 0:
                         data.append({
                        'date': record.date,
                        'date_fat': record.date_piece,
                        'journal_id': record.journal_id.id,
                        'company_id': record.company_id.id,
                        'ref': record.reference,
                        'invoice_id': data_line.account_invoice_id.id,
                        'retenu_source_id': record.id,
                        'line_ids': [(0, 0,
                                {   # ++==++  TVA ++==++
                                    'account_id': account_tva_id,
                                    'partner_id': record.partner_id.id,
                                    'name': record.reference,
                                    'no_facture': data_line.account_invoice_id.number.split('/')[-1],
                                    'date_facture': record.date_piece,
                                    'ref_facture': record.reference,
                                    'debit': data_line.tva_recu,
                                }),
                                (0, 0, {   # ++==++ Ajustement TVA ++==++
                                    'account_id': account_tva_id,
                                    'partner_id': record.partner_id.id,
                                    'name': record.reference,
                                    'no_facture': data_line.account_invoice_id.number.split('/')[-1],
                                    'date_facture': record.date_piece,
                                    'ref_facture': record.reference,
                                    'debit': (data_line.tva_aj if data_line.tva_aj > 0 else 0),
                                    'credit': (-data_line.tva_aj if data_line.tva_aj < 0 else 0),
                                }) ,
                                (0, 0, {   # ++==++ A/IR ++==++
                                    'account_id': account_ir_id,
                                    'partner_id': record.partner_id.id,
                                    'name': record.reference,
                                    'no_facture': data_line.account_invoice_id.number.split('/')[-1],
                                    'date_facture': record.date_piece,
                                    'ref_facture': record.reference,
                                    'debit': data_line.ir_recu,
                                    'credit': 0
                                }),
                                (0, 0, {   # ++==++ Compte du tiers ++==++
                                    'account_id': account_partner_id,
                                    'partner_id': record.partner_id.id,
                                    'name': record.reference,
                                    'no_facture': data_line.account_invoice_id.number.split('/')[-1] ,
                                    'date_facture': record.date_piece,
                                    'ref_facture': record.reference,
                                    "credit": sum([data_line.tva_recu, data_line.tva_aj, data_line.ir_recu, data_line.ir_aj])
                                })

                            ]
                    })


                    elif data_line.tva_aj == 0  and data_line.ir_aj != 0:
                         data.append({
                        'date': record.date,
                        'date_fat': record.date_piece,
                        'journal_id': record.journal_id.id,
                        'company_id': record.company_id.id,
                        'ref': record.reference,
                        'invoice_id': data_line.account_invoice_id.id,
                        'retenu_source_id': record.id,
                        'line_ids': [(0, 0,
                                {   # ++==++  TVA ++==++
                                    'account_id': account_tva_id,
                                    'partner_id': record.partner_id.id,
                                    'name': record.reference,
                                    'no_facture': data_line.account_invoice_id.number.split('/')[-1],
                                    'date_facture': record.date_piece,
                                    'ref_facture': record.reference,
                                    'debit': data_line.tva_recu,
                                }),
                                (0, 0, {   # ++==++ A/IR ++==++
                                    'account_id': account_ir_id,
                                    'partner_id': record.partner_id.id,
                                    'name': record.reference,
                                    'no_facture': data_line.account_invoice_id.number.split('/')[-1],
                                    'date_facture': record.date_piece,
                                    'ref_facture': record.reference,
                                    'debit': data_line.ir_recu,
                                    'credit': 0
                                }),
                                (0, 0, {   # ++==++ Ajustement A/IR ++==++
                                    'account_id': account_tva_id,
                                    'partner_id': record.partner_id.id,
                                    'name': record.reference,
                                    'no_facture': data_line.account_invoice_id.number.split('/')[-1],
                                    'date_facture': record.date_piece,
                                    'ref_facture': record.reference,
                                    'debit': (data_line.ir_aj if data_line.ir_aj > 0 else 0),
                                    'credit': (-data_line.ir_aj if data_line.ir_aj < 0 else 0),
                                }),
                                (0, 0, {   # ++==++ Compte du tiers ++==++
                                    'account_id': account_partner_id,
                                    'partner_id': record.partner_id.id,
                                    'name': record.reference,
                                    'no_facture': data_line.account_invoice_id.number.split('/')[-1] ,
                                    'date_facture': record.date_piece,
                                    'ref_facture': record.reference,
                                    "credit": sum([data_line.tva_recu, data_line.tva_aj, data_line.ir_recu, data_line.ir_aj])
                                })

                            ]
                    })

                    else:
                         data.append({
                        'date': record.date,
                        'date_fat': record.date_piece,
                        'journal_id': record.journal_id.id,
                        'company_id': record.company_id.id,
                        'ref': record.reference,
                        'invoice_id': data_line.account_invoice_id.id,
                        'retenu_source_id': record.id,
                        'line_ids': [(0, 0,
                                {   # ++==++  TVA ++==++
                                    'account_id': account_tva_id,
                                    'partner_id': record.partner_id.id,
                                    'name': record.reference,
                                    'no_facture': data_line.account_invoice_id.number.split('/')[-1],
                                    'date_facture': record.date_piece,
                                    'ref_facture': record.reference,
                                    'debit': data_line.tva_recu,
                                }),
                                (0, 0, {   # ++==++ Ajustement TVA ++==++
                                    'account_id': account_tva_id,
                                    'partner_id': record.partner_id.id,
                                    'name': record.reference,
                                    'no_facture': data_line.account_invoice_id.number.split('/')[-1],
                                    'date_facture': record.date_piece,
                                    'ref_facture': record.reference,
                                    'debit': (data_line.tva_aj if data_line.tva_aj > 0 else 0),
                                    'credit': (-data_line.tva_aj if data_line.tva_aj < 0 else 0),
                                }) ,
                                (0, 0, {   # ++==++ A/IR ++==++
                                    'account_id': account_ir_id,
                                    'partner_id': record.partner_id.id,
                                    'name': record.reference,
                                    'no_facture': data_line.account_invoice_id.number.split('/')[-1],
                                    'date_facture': record.date_piece,
                                    'ref_facture': record.reference,
                                    'debit': data_line.ir_recu,
                                    'credit': 0
                                }),
                                (0, 0, {   # ++==++ Ajustement A/IR ++==++
                                    'account_id': account_tva_id,
                                    'partner_id': record.partner_id.id,
                                    'name': record.reference,
                                    'no_facture': data_line.account_invoice_id.number.split('/')[-1],
                                    'date_facture': record.date_piece,
                                    'ref_facture': record.reference,
                                    'debit': (data_line.ir_aj if data_line.ir_aj > 0 else 0),
                                    'credit': (-data_line.ir_aj if data_line.ir_aj < 0 else 0),
                                }),
                                (0, 0, {   # ++==++ Compte du tiers ++==++
                                    'account_id': account_partner_id,
                                    'partner_id': record.partner_id.id,
                                    'name': record.reference,
                                    'no_facture': data_line.account_invoice_id.number.split('/')[-1] ,
                                    'date_facture': record.date_piece,
                                    'ref_facture': record.reference,
                                    "credit": sum([data_line.tva_recu, data_line.tva_aj, data_line.ir_recu, data_line.ir_aj])
                                })

                            ]
                    })

                    model_account_invoice = self.env['account.invoice'].search(
                                [
                                    ('id', "=", data_line.account_invoice_id.id)
                                ], limit=1
                            ).write(
                                {
                                    'retenue_source_id': record.id,
                                }
                            )  

            model_account = self.env['account.move'].create(data)
            self.write(
                {
                    'state': 'valide',
                }
            )
            
    def cancel(self):
        model_account_move = self.env['account.move'].search(
             [
                ("retenu_source_id", "=", self.id)
             ]
        )
        for record in model_account_move:
            record.unlink()

        # ++++==++++++ PROBLEME OF RIGHT WENT TRYING TO DELETE ASSOCIATE RECORD ===+++++====
        mode_account_invoice = self.env['account.invoice'].search(
            [
                ('retenue_source_id', '=', self.id)
            ]
        ).write(
            {
                'retenue_source_id': None
            }
        )
            
        if self.state == "valide":
            self.write(
                {
                    'state': 'draft', 
                }
            )
            
    def action_a_approuver(self):
        self.write(
            {
                'state': 'to_approuv',
            }
        )


    @api.depends('line_ids')
    def _comute_amount_total(self):
        for record in self:
            record.montant_total = sum((el.tva_recu + el.ir_recu) for el in record.line_ids)


    def get_initiaux(self, nom):
        list_nom = nom.split(' ')
        if len(list_nom) <= 1:
            res = list_nom[0][:5]
            return res.upper()
        else:
            res = str(list_nom[0][:1])+"."+ str(list_nom[1][:5]) 
            return res.upper() 


    @api.one
    @api.depends('journal_id')
    def _compute_currency(self):
        self.currency_id = self.journal_id.currency_id or self.company_id.currency_id
    

    def cancel1(self):
        for record in self:
            if record.state == "to_approuv":
                record.write(
                    {
                        'state': 'draft',
                    }
                )