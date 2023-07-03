import os
import json
import shutil

from src.common.util import AppConfig


def init_folder():
    # 检查文件夹是否存在，如果不存在则创建
    if not os.path.exists(AppConfig.get_input_path()):
        os.makedirs(AppConfig.get_input_path())

    if not os.path.exists(AppConfig.output_path):
        os.makedirs(AppConfig.output_path)

    # 检查data.json文件是否存在，如果不存在则创建空的json文件
    if not os.path.exists(AppConfig.data_path):
        with open(AppConfig.data_path, "w") as f:
            json.dump({}, f)


def clear_folder():
    # 删除文件夹及其内容
    shutil.rmtree(AppConfig.output_path)

    # 创建新的空文件夹
    os.makedirs(AppConfig.output_path)

    with open(AppConfig.data_path, "w") as f:
        json.dump({}, f)
