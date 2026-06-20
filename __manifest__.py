# -*- coding: utf-8 -*-
##############################################################################
#                 @author IT Admin
#
##############################################################################

{
    'name': 'Formato de reporte de factura Sincro',
    'version': '18.0.1.0.0',
    'description': ''' Invoice report
    ''',
    'category': 'Accounting',
    'author': 'SINCRO Recursos Digitales',
    'website': 'sincro.com.mx',
    'depends': [
        'base',
        'account','cdfi_invoice','purchase',
    ],
    'data': [
        'report/invoice_report_custom.xml'],
    'application': False,
    'installable': True,
    'price': 0.00,
    'currency': 'USD',
    'license': 'OPL-1',	
}
