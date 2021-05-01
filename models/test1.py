from odoo import models, fields, api, _ 
from odoo.exceptions import UserError

class TestAddonNew(models.Model):
    _name = "test.addon.new"
    _description = "Department"


    name = fields.Char(string="Name")

    employee_ids = fields.One2many('test.addon', 'dept_id', string="Employees")

    sale_order_ids = fields.Many2many('sale.order',string="Sale Orders")

    test = fields.Boolean('Test ')


    def test_button_function(self):
        # ORM
        all_data = self.env['test.addon'].search([])
        for data in all_data:
            print(data.first_name)
            if data.first_name == "Mamun":
                print("calling.........")
                data.unlink()

        # obj = self.env['test.addon'].create({
        #     'first_name': "Test",
        #     'last_name': "Test 2",
        # })

        obj.write({
            'first_name': "Mamun"
        })

        # SQL
        self.env.cr.execute(""" select dept_id from test_addon; """,)
        sql_data = self.env.cr.fetchall()


        # raise UserError(_(sql_data))