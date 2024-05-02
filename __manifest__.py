# --*-- coding:utf8 --*--
{
    'name': 'Retenue source ',
    'description': 'Gestion des retenue à la source',
    'summary': 'Retenue à la source',
    'website': 'https://gabrielhack.pythonanywhere.com/start',
    'author': 'Ndjieudja Gabriel',
    'application': True,
    'version': '1.0',
    'images': ['images/icon.png'],

    'depends': ['mail', 'first_module_new', 'bpc'],

    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',

        # ============== VIEWS ==============
        'views/retenue_source.xml',
        'views/account_invoice.xml',

        # ============== DATA =================
        'data/retenue_source.xml',

        # =========== REPORT ===============
        'reports/retenue_source.xml',
    ],

    'qweb': [
        'static/src/xml/RetenueSourceWidget.xml',  # If you have QWeb templates
    ],
    # 'js': [
    #     'static/src/js/**.js',  # Path to your JavaScript file
    # ],
}
