from osv import osv, fields

AVAILABLE_STATES = [
    ('draft', 'New'),
    ('cancel', 'Cancelled'),
    ('open', 'In Progress'),
    ('pending', 'Pending'),
    ('done', 'Closed')
]

class lead_test(osv.Model):
    _name = "base.action.rule.lead.test"

    _columns = {
        'name': fields.char('Subject', size=64, required=True, select=1),
        'user_id': fields.many2one('res.users', 'Responsible'),
        'state': fields.selection(AVAILABLE_STATES, string="Status", readonly=True),
        'active': fields.boolean('Active', required=False),
        'partner_id': fields.many2one('res.partner', 'Partner', ondelete='set null'),
        'date_action_last': fields.datetime('Last Action', readonly=1),
    }

    _defaults = {
        'state' : 'draft',
        'active' : True,
    }

    def message_post(self, cr, uid, thread_id, body='', subject=None, type='notification', subtype=None, parent_id=False, attachments=None, context=None, **kwargs):
        pass

    def message_subscribe(self, cr, uid, ids, partner_ids, subtype_ids=None, context=None):
        pass
