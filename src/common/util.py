
import os
import sys

main_path = os.path.join(os.path.dirname(
    os.path.abspath(__file__)), '..', '..')
if getattr(sys, 'frozen', False):
    main_path = os.path.join(sys._MEIPASS, '..')

input_path = os.path.join(main_path, 'origin')
output_path = os.path.join(main_path, 'source')
data_path = os.path.join(main_path, 'data.json')
pdf_suffix = '.pdf'
txt_suffix = '.txt'
