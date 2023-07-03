import os
import pdfplumber
import unicodedata

from src.common.util import AppConfig

if AppConfig.use_ocr:
    from pdf2image import convert_from_path
    import pytesseract
    from PIL import Image


class PdfProcess:
    def __init__(self, output_folder):
        self.output_folder = output_folder

    def convert_to_txt(self, pdf_path):
        file_name = os.path.basename(pdf_path)
        if file_name.endswith('.pdf'):
            output_file_name = file_name[:-4] + '.txt'
            output_path = os.path.join(self.output_folder, output_file_name)

            # 使用pdfplumber提取文本
            with pdfplumber.open(pdf_path) as pdf:
                text = ""
                for page in pdf.pages:
                    text += page.extract_text()

            # 如果提取的文本为空，则使用pdf2image和pytesseract进行OCR识别
            if AppConfig.use_ocr and not text.strip():
                images = convert_from_path(pdf_path)
                for i, image in enumerate(images):
                    image_path = os.path.join(
                        self.output_folder, f"page_{i+1}.png")
                    image.save(image_path, 'PNG')

                    image_text = pytesseract.image_to_string(
                        Image.open(image_path), lang='chi_sim')
                    text += image_text.strip()

                    os.remove(image_path)  # 删除生成的图片

            # 去除空格和换行符
            text = text.replace(" ", "").replace("\n", "")
            text = unicodedata.normalize('NFKC', text)

            with open(output_path, 'w', encoding='utf-8') as txt_file:
                txt_file.write(text)
