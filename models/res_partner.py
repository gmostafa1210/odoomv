from odoo import models, fields, api, _ 
from odoo.exceptions import UserError

class ResPartner(models.Model):
    _inherit = "res.partner"


    fax_no = fields.Char(string="Fax No")

    def fax_check_validation(self):
        if self.fax_no and len(self.fax_no)>3:
            raise UserError(_("You can input only 3 digits"))

    # @api.onchange('fax_no')
    # def onchange_fax_no(self):
    #     self.fax_check_validation()


    def write(self, values):
        
        res = super(ResPartner, self).write(values)
        self.fax_check_validation()

        # print("++++++++\n\n",values)
        # print(self.fax_no)
        # self.fax_check_validation()
        return res 