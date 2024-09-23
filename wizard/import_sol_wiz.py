import base64
import io
import xlrd
from odoo import fields, models, api, _
from odoo.exceptions import UserError


class ImportSOLWiz(models.TransientModel):
    _name = 'import.sol.wiz'
    _description = 'Import Sale Order Line Wizard'

    so_id = fields.Many2one("sale.order", string="Sale Order", default=lambda self: self._default_so_id())
    customer_name = fields.Many2one('res.partner', related='so_id.partner_id', string="Partner Name")
    import_file = fields.Binary("Upload XLSX")
    message = fields.Html("Response")
    message_type = fields.Selection([("import", "Import"), ("success", "Success")], default="import")

    @api.model
    def _default_so_id(self):
        return self.env.context.get('active_id') if self.env.context.get('active_model') == 'sale.order' else None

    def download_sample_file(self):
        return self.env.ref("sha_import_order_lines.sample_sol_xlsx").report_action(self)

    def import_xlsx_file(self):
        if not self.import_file:
            raise UserError(_("No XLSX file is uploaded! Please upload a XLSX file to import."))

        try:
            inputx = io.BytesIO(base64.decodebytes(self.import_file))
            workbook = xlrd.open_workbook(file_contents=inputx.getvalue())
        except Exception as e:
            raise UserError(_("File Error: {}".format(e)))

        sheet = workbook.sheet_by_index(0)
        message_lines, order_lines = [], []
        product_product = self.env['product.product']

        for row in range(1, sheet.nrows):
            product_name = sheet.cell(row, 0).value
            default_code = sheet.cell(row, 1).value
            try:
                quantity = float(sheet.cell(row, 2).value)
                unit_price = float(sheet.cell(row, 3).value)
            except ValueError as e:
                message_lines.append(f"<p>Line {row + 1}: Invalid data format for '{product_name}' - {str(e)}</p>")
                continue

            product = product_product.search([("default_code", "=", default_code)], limit=1)
            if not product:
                product = product_product.search([("name", "=", product_name)], limit=1)
            if not product:
                message_lines.append(
                    f"<p><span style='display: inline-block; width: 15px; height: 15px; background-color: red; border-radius: 50%; color: white; text-align: center; line-height: 15px;'>&#10006;</span> Line {row + 1}: Not Found '{product_name}'</p>")
                continue

            order_lines.append((0, 0, {
                "product_id": product.id,
                "product_uom_qty": quantity,
                "price_unit": unit_price,
            }))
            message_lines.append(
                f"<p><span style='display: inline-block; width: 15px; height: 15px; background-color: green; border-radius: 50%; color: white; text-align: center; line-height: 15px;'>&#10004;</span> Line {row + 1}: Imported '{product_name}'</p>")

        if order_lines:
            self.so_id.write({"order_line": order_lines})

        return {
            "type": "ir.actions.act_window",
            "name": "Import Order Lines",
            "res_model": self._name,
            "view_mode": "form",
            "target": "new",
            "context": {"default_message": ''.join(message_lines), "default_message_type": "success"},
        }
