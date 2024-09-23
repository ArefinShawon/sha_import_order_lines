from odoo import fields, models, api


class ImportPOLXLSX(models.AbstractModel):
    _name = 'report.download_sample_pol_xlsx'
    _inherit = "report.report_xlsx.abstract"
    _description = 'Download Sample POL XLSX'

    @api.model
    def _get_report_values(self, data=None):
        return {"report_data": data}

    def generate_xlsx_report(self, workbook, data, records):
        sheet = workbook.add_worksheet("Purchase Order Lines")
        sheet.set_column(0, 3, 20)
        bold = workbook.add_format({"bold": True})

        sheet.write(0, 0, "Product Name", bold)
        sheet.write(0, 1, "Product Code", bold)
        sheet.write(0, 2, "Quantity", bold)
        sheet.write(0, 3, "Unit Price", bold)

        SAMPLE_DATA = [
            {
                "product": "Office Lamp",
                "default_code": "FURN_8888",
                "quantity": 9,
                "unit_price": 58.00,
            },
            {
                "product": "Office Chair",
                "default_code": "FURN_7777",
                "quantity": 3,
                "unit_price": 65.00,
            },
        ]

        row = 1

        for data in SAMPLE_DATA:
            sheet.write(row, 0, data["product"])
            sheet.write(row, 1, data["default_code"])
            sheet.write(row, 2, data["quantity"])
            sheet.write(row, 3, data["unit_price"])
            row += 1
