#--------------------------------------------------------------------------
#     This file is part of BKchem - a chemical drawing program
#     Copyright (C) 2002, 2003 Beda Kosata <beda@zirael.org>

#     This program is free software; you can redistribute it and/or modify
#     it under the terms of the GNU General Public License as published by
#     the Free Software Foundation; either version 2 of the License, or
#     (at your option) any later version.

#     This program is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU General Public License for more details.

#     Complete text of GNU GPL can be found in the file gpl.txt in the
#     main directory of the program

#--------------------------------------------------------------------------
#
# Last edited: $Date: 2003/09/26 10:47:02 $
#
#--------------------------------------------------------------------------

"""similar to periodic table but for common functional groups. Keys are in lowercase form."""

groups_table = {'och3':   { 'name': 'OCH3', 'textf': 'OCH<sub>3</sub>',
                            'textb': 'H<sub>3</sub>CO', 'composition': 'OCH3'},

                'no2':    { 'name': 'NO2',  'textf': 'NO<sub>2</sub>',
                            'textb': 'O<sub>2</sub>N', 'composition': 'NO2'},

                'cooh':   { 'name': 'COOH', 'textf': 'COOH',
                            'textb': 'HOOC', 'composition': 'COOH'},

                'cooch3': { 'name': 'COOCH3', 'textf': 'COOCH<sub>3</sub>',
                            'textb': 'H<sub>3</sub>COOC', 'composition': 'COOCH3'},

                'me': { 'name': 'Me', 'textf': 'Me',
                        'textb': 'Me', 'composition': 'CH3'},

                'cn': { 'name': 'CN', 'textf': 'CN',
                        'textb': 'NC', 'composition': 'CN'},

                'so3h': { 'name': 'SO3H', 'textf': 'SO<sub>3</sub>H',
                          'textb': 'H<sub>3</sub>OS', 'composition': 'SO3H'},

                'pph3': { 'name': 'PPh3', 'textf': 'PPh<sub>3</sub>',
                          'textb': 'Ph<sub>3</sub>P', 'composition': 'C18H15P'},

                'ome': { 'name': 'OMe', 'textf': 'OMe',
                         'textb': 'MeO', 'composition': 'OCH3'},

                'et': { 'name': 'Et', 'textf': 'Et',
                         'textb': 'Et', 'composition': 'C2H5'},

                'ph': { 'name': 'Ph', 'textf': 'Ph',
                         'textb': 'Ph', 'composition': 'C6H5'},

                'cocl': { 'name': 'COCl', 'textf': 'COCl',
                         'textb': 'ClOC', 'composition': 'COCl'},


                }



