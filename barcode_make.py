import barcode
from barcode.writer import ImageWriter
from barcode import generate
import sys

bar_code = sys.argv[1]
code_format = 'isbn13'

bar_code_class = barcode.get_barcode_class(code_format) 
bar_code_make = bar_code_class(bar_code, writer=ImageWriter()) 
bar_code_png = bar_code_make.save('barcode') 
bar_code_svg = generate(code_format, bar_code, output='barcode')