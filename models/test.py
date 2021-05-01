from odoo import models, fields, api, _ 
from odoo.exceptions import UserError


# class BistaEmployee(models.Model):
#     _name = 'bista.employee'

    # Extension 

    # dept_id = fields.Many2one()



class TestAddon(models.Model):
    _name = "test.addon"
    _description = "Employee"


    first_name = fields.Char('Frist Name')
    last_name = fields.Char('Last Name')
    name = fields.Char(string="Name", compute="_get_full_name")
    age = fields.Integer(string="AGE")
    address = fields.Text(string="Address")
    dept = fields.Selection([('backend',"Back-End"),
                            ('qa',"QA"),
                            ('sales','Sales')],
                            string="Department"
                            )
    
    have_address = fields.Boolean(string="Have Address")
    
    dept_id = fields.Many2one('test.addon.new', string="Dept.", domain=[('test','=',True)])



    # dept_ids = fields.Many2many('test.addon.new', string="Multi-Depts")

    def full_name(self):
        first_name = ""
        last_name = ""
        if self.first_name:
            first_name = self.first_name
        if self.last_name:
            last_name = self.last_name
        return first_name + " " + last_name

    def _get_full_name(self):
        for item in self:
            item.name = item.full_name()

    @api.model
    def create(self, values):
        print("++++++\n", values)
        values['age'] = 32
        result = super(TestAddon, self).create(values)
        return result
    

    def write(self, values):
        print("++++++\n", values)
        values['age'] = 40
        result = super(TestAddon, self).write(values)
        return result

    @api.onchange('first_name','last_name')
    def onchange_name(self):
        self.name = self.full_name()
    
    @api.onchange('age')
    def onchange_age(self):
        # if self.age < 18:
        #     raise UserError(_("You are under age"))
        print("+++++++++++++++++++++++ \nCalling Onchange AGE function\n",self.address)
        self.address="Dinajpur"
        pass
