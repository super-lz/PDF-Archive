import os
import json

class FolderTraverser:
    def __init__(self, folder_path, suffix):
        self.folder_path = folder_path
        self.file_names = []
        self.suffix = suffix

    def find_files(self):
        self.file_names = []
        for root, dirs, files in os.walk(self.folder_path):
            for file in files:
                if file.lower().endswith(self.suffix):  # 判断文件是否是 PDF 文件
                    file_name = os.path.splitext(file)[0]
                    self.file_names.append(file_name)

    def save_to_json(self, json_file_path):
        with open(json_file_path, 'w') as json_file:
            json.dump(self.file_names, json_file)


