from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class HelpdeskTicket(models.Model):
    _name = 'helpdesk.ticket'
    _description = 'Helpdesk Ticket'
    _inherit = ['mail.thread', 'mail.activity.mixin', 'portal.mixin']
    _order = 'priority desc, id desc'
    _rec_name = 'name'

    name = fields.Char(
        string='Subject',
        required=True,
        tracking=True,
        help="Brief description of the issue"
    )
    
    description = fields.Html(
        string='Description',
        help="Detailed description of the issue"
    )
    
    partner_id = fields.Many2one(
        'res.partner',
        string='Customer',
        required=True,
        tracking=True,
        help="Customer who reported the issue"
    )
    
    partner_email = fields.Char(
        related='partner_id.email',
        string='Customer Email',
        readonly=True
    )
    
    team_id = fields.Many2one(
        'helpdesk.team',
        string='Team',
        required=True,
        tracking=True,
        help="Team responsible for handling this ticket"
    )
    
    user_id = fields.Many2one(
        'res.users',
        string='Assigned To',
        tracking=True,
        help="User assigned to handle this ticket"
    )
    
    stage_id = fields.Many2one(
        'helpdesk.stage',
        string='Stage',
        required=True,
        tracking=True,
        group_expand='_read_group_stage_ids',
        help="Current stage of the ticket"
    )
    
    priority = fields.Selection([
        ('0', 'Low'),
        ('1', 'Normal'),
        ('2', 'High'),
        ('3', 'Urgent'),
    ], string='Priority', default='1', tracking=True)
    
    tag_ids = fields.Many2many(
        'helpdesk.tag',
        string='Tags',
        help="Tags for categorizing tickets"
    )
    
    company_id = fields.Many2one(
        'res.company',
        string='Company',
        default=lambda self: self.env.company
    )
    
    active = fields.Boolean(default=True)
    
    color = fields.Integer(string='Color Index')
    
    kanban_state = fields.Selection([
        ('normal', 'In Progress'),
        ('done', 'Ready'),
        ('blocked', 'Blocked'),
    ], string='Kanban State', default='normal')
    
    # Computed fields
    stage_name = fields.Char(related='stage_id.name', string='Stage Name', readonly=True)
    
    @api.model
    def _read_group_stage_ids(self, stages, domain, order):
        """Return all stages for kanban view"""
        return stages.search([], order=order)
    
    @api.model
    def create(self, vals):
        """Override create to set default stage"""
        if not vals.get('stage_id'):
            default_stage = self.env['helpdesk.stage'].search([('is_default', '=', True)], limit=1)
            if default_stage:
                vals['stage_id'] = default_stage.id
        return super().create(vals)
    
    def action_assign_to_me(self):
        """Assign ticket to current user"""
        self.write({'user_id': self.env.user.id})
    
    def action_close_ticket(self):
        """Close the ticket"""
        closed_stage = self.env['helpdesk.stage'].search([('is_closed', '=', True)], limit=1)
        if closed_stage:
            self.write({'stage_id': closed_stage.id})
    
    def _compute_access_url(self):
        """Compute portal access URL"""
        super()._compute_access_url()
        for ticket in self:
            ticket.access_url = '/my/tickets/%s' % ticket.id


class HelpdeskTeam(models.Model):
    _name = 'helpdesk.team'
    _description = 'Helpdesk Team'
    _order = 'sequence, name'

    name = fields.Char(string='Team Name', required=True)
    description = fields.Text(string='Description')
    sequence = fields.Integer(string='Sequence', default=10)
    active = fields.Boolean(default=True)
    
    member_ids = fields.Many2many(
        'res.users',
        string='Team Members',
        help="Users who are members of this team"
    )
    
    color = fields.Integer(string='Color Index')
    
    # Statistics
    ticket_count = fields.Integer(
        string='Ticket Count',
        compute='_compute_ticket_count'
    )
    
    @api.depends('member_ids')
    def _compute_ticket_count(self):
        """Compute number of tickets for this team"""
        for team in self:
            team.ticket_count = self.env['helpdesk.ticket'].search_count([
                ('team_id', '=', team.id)
            ])


class HelpdeskStage(models.Model):
    _name = 'helpdesk.stage'
    _description = 'Helpdesk Stage'
    _order = 'sequence, name'

    name = fields.Char(string='Stage Name', required=True)
    description = fields.Text(string='Description')
    sequence = fields.Integer(string='Sequence', default=10)
    active = fields.Boolean(default=True)
    
    is_default = fields.Boolean(
        string='Default Stage',
        help="New tickets will be assigned to this stage by default"
    )
    
    is_closed = fields.Boolean(
        string='Closed Stage',
        help="Tickets in this stage are considered closed"
    )
    
    fold = fields.Boolean(
        string='Folded in Kanban',
        help="This stage is folded in the kanban view when there are no records in that stage to display."
    )


class HelpdeskTag(models.Model):
    _name = 'helpdesk.tag'
    _description = 'Helpdesk Tag'
    _order = 'name'

    name = fields.Char(string='Tag Name', required=True)
    color = fields.Integer(string='Color Index')
    active = fields.Boolean(default=True)
