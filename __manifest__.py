{
    'name': 'Print form Invoice for Ukraine',
    'summary': 'Print forms Rahunok and Akt in Invoice for Ukraine',
    'author': 'Mikola Ostroukh',
    'license': "LGPL-3",
    'category': 'Accounting',
    'version': '15.0.1.0.0',
    'depends': ['base', 'account'],
    'data': [
        'views/res_company_views.xml',
        'views/res_partner_views.xml',
        'views/res_bank_views.xml',
        'report/invoice_report_views.xml',
        'report/invoice_report_rah_templates.xml',
        'report/invoice_report_akt_templates.xml',
        'report/invoice_report_invoice_ua_templates.xml',
    ],
    'external_dependencies': {
        'python': [
            'num2words',
        ],
    },
}
