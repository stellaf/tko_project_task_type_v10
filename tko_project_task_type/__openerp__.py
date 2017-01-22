# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
#    ThinkOpen Solutions Brasil
#    Copyright (C) Thinkopen Solutions <http://www.tkobr.com>.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'Project task type with colours',
    'version': '10.003',
    'category': 'Customizations',
    'sequence': 14,
    'complexity': 'medium',
    'description': '''== This module adds a task type field works for V10==\n
Each type will have a colour. This makes easy to identify the tasks types in kanban through their colours.''',
    'author': 'ThinkOpen Solutions Brasil',
    'website': 'http://www.tkobr.com',
    'depends': [
                'base',
                'project',
    ],
    'data': [
        'security/ir.model.access.csv',
        'project_task_view.xml',
    ],
    'init': [],
    'demo': [],
    'update': [],
    'test': [],  # YAML files with tests
    'installable': True,
    'application': False,
    # If it's True, the modules will be auto-installed when all dependencies
    # are installed
    'auto_install': False,
    'certificate': '',
}
