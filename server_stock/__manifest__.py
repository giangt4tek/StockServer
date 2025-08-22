{# Part of Odoo. See LICENSE file for full copyright and licensing details.
 # Tên module
    'name': 'Server Stock',
    'version': '18.0',

    # Loại module
    'category': 'stock',


    # Độ ưu tiên module trong list module
    # Số càng nhỏ, độ ưu tiên càng cao
    #### Chấp nhận số âm
    #'sequence': 5,

    # Mô tả module
    "summary": "Debt recording system and payment call",
    'description': 'Kho quản lý linh kiện thiết bị máy server',
    'author': 'GinGa GX',

    "depends": [
        "base"
    ],
    
    
    "data": [
        # 'security/access_user.xml',
        # 'security/ir.model.access.csv',
        # 'views/pos_category.xml',
        # 'views/invoice_report.xml',
        # 'views/wallet_contact.xml',
        # 'data/cron_invoice.xml',
        # 'views/menu_item.xml',
       
        
        
    ],

    'assets': {
        'web.assets_backend':
        [
            'server_stock/static/src/js/**/*',
            'server_stock/static/src/xml/**/*',
        ],
#         
    },
    "installable": True,
    "license": "LGPL-3",
}
