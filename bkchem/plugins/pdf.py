#--------------------------------------------------------------------------
#     This file is part of BKchem - a chemical drawing program
#     Copyright (C) 2004  Beda Kosata <beda@zirael.org>

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


from piddle_lowlevel import piddle_exporter
from piddle import piddlePDF


class pdf_exporter( piddle_exporter):


  def init_canvas( self, pagesize=None):
    return piddlePDF.PDFCanvas( pagesize=pagesize)



# PLUGIN INTERFACE SPECIFICATION
name = "PDF"
extensions = [".pdf"]
exporter = pdf_exporter