from odoo import models


class PurchaseOrderLineImport(models.Model):
    _inherit = "purchase.order"

    def import_lines(self):
        return {
            "type": "ir.actions.act_window",
            "name": "Import Purchase Order Lines",
            "res_model": "import.pol.wiz",
            "view_mode": "form",
            "target": "new",
            "context": {"default_purchase_id": self.id},
        }
