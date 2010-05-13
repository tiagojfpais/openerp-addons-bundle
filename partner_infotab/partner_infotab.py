# -*- coding: utf-8 -*-
##############################################################################
#    
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.     
#
##############################################################################

from osv import osv, fields

class res_partner(osv.osv):
    """ Inherits partner and adds more information in the partner form """
    _inherit = 'res.partner'
    
    _columns = {
                'opportunity_ids': fields.one2many('crm.lead', 'partner_id', 'Opportunities', domain=[('type', '=', 'opportunity')]), 
                'meeting_ids': fields.one2many('crm.meeting', 'partner_id',\
                                                     'Meetings'), 
                'phonecall_ids': fields.one2many('crm.phonecall', 'partner_id', 'Phonecalls'), 
                'invoice_ids': fields.one2many('account.invoice.line', 'partner_id', 'Invoices'), 
                'contract_ids': fields.one2many('account.analytic.account', \
                                                    'partner_id', 'Contracts'), 
                'account_line_ids': fields.one2many('hr.analytic.timesheet', \
                                                    'partner_id', 'Anaylitic account lines '),
                }

res_partner()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
