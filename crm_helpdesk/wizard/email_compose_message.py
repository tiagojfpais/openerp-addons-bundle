# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2010-Today OpenERP SA (<http://www.openerp.com>)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>
#
##############################################################################

from osv import osv
from osv import fields
import tools

class email_compose_message(osv.osv_memory):
    _inherit = 'mail.compose.message'

    def get_value(self, cr, uid, model, resource_id, context=None):
        '''
        """Returns a defaults-like dict with initial values for the composition
           wizard when sending an email related to the document record identified
           by ``model`` and ``res_id``.

           Overrides the default implementation to provide more default field values
           related to the corresponding CRM case.

           :param str model: model name of the document record this mail is related to.
           :param int res_id: id of the document record this mail is related to.
           :param dict context: several context values will modify the behavior
                                of the wizard, cfr. the class description.
        '''
        if context is None:
            context = {}
        result = super(email_compose_message, self).get_value(cr, uid,  model, resource_id, context=context)
        if model == 'crm.helpdesk' and resource_id:
            model_obj = self.pool.get(model)
            data = model_obj.browse(cr, uid , resource_id, context)
            result.update({
                    'subject' : data.name or False,
                    'email_to' : data.email_from or False,
                    'email_from' : data.user_id and data.user_id.address_id and data.user_id.address_id.email or False,
                    'body_text' : '\n' + (tools.ustr(data.user_id.signature or '')),
                    'email_cc' : tools.ustr(data.email_cc or ''),
                    'model': model,
                    'res_id': resource_id,
                })
        return result

email_compose_message()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
