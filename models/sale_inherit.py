from odoo import models


class SaleOrderLineImport(models.Model):
    _inherit = "sale.order"

    def import_lines(self):
        return {
            "type": "ir.actions.act_window",
            "name": "Import Sale Order Lines",
            "res_model": "import.sol.wiz",
            "view_mode": "form",
            "target": "new",
            "context": {"default_sale_id": self.id},
        }
