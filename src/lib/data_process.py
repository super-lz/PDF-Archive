import os

from src.common.folder_traverser import FolderTraverser
from src.common.pdf_process import PdfProcess
from src.common.json_process import JsonProcess
from src.common.util import AppConfig

def process_data():
    origin_folder = FolderTraverser(AppConfig.get_input_path(), AppConfig.pdf_suffix)
    source_folder = FolderTraverser(AppConfig.output_path, AppConfig.txt_suffix)
    pdf_process = PdfProcess(AppConfig.output_path)
    json_process = JsonProcess(AppConfig.data_path)

    origin_folder.find_files()
    source_folder.find_files()

    # ==== 生成source ====
    # 转换还未转换的文件
    for file_name in origin_folder.file_names:
        if file_name not in source_folder.file_names:
            print(f'add:{file_name}')
            file_path = os.path.join(AppConfig.get_input_path(), file_name + AppConfig.pdf_suffix)
            pdf_process.convert_to_txt(file_path)
            source_folder.file_names.append(file_name)

    # 去除多余的文件
    for file_name in source_folder.file_names:
        if file_name not in origin_folder.file_names:
            print(f'remove:{file_name}')
            file_path = os.path.join(AppConfig.output_path, file_name + AppConfig.txt_suffix)
            os.remove(file_path)
            source_folder.file_names.remove(file_name)

    # ==== 生成data ====
    # 添加还未添加的数据
    for file_name in source_folder.file_names:
        if not json_process.object_exists(file_name):
            file_path = os.path.join(AppConfig.output_path, file_name + AppConfig.txt_suffix)
            json_process.add_object(file_name, file_path)

    # 移除多余的数据
    for obj in json_process.data:
        if obj['name'] not in source_folder.file_names:
            json_process.delete_object(obj['name'])

    json_process.save_data()
