from pdf2image import convert_from_path
from wand.image import Image

import tempfile

images = convert_from_path('pdf/domingo v2 - Tenor Saxophone.pdf', output_folder='images', fmt='jpeg', output_file='lala')

# for image in images:
#     with Image(filename=image) as img:
#         img.format = 'jpeg'
#         img.save(filename='result/teste.png')