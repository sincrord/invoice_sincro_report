# -*- coding: utf-8 -*-
##############################################################################
#                 @author IT Admin
#
##############################################################################

{
    'name': 'Formato de reporte de factura Sincro',
    'version': '11.4',
    'description': ''' Invoice report
    ''',
    'category': 'Accounting',
    'author': 'IT Admin',
    'website': 'www.itadmin.com.mx',
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
