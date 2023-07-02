import os
import json
from src.common.util import input_path, output_path, data_path


def init_folder():
    # 检查文件夹是否存在，如果不存在则创建
	if not os.path.exists(input_path):
		os.makedirs(input_path)

	if not os.path.exists(output_path):
		os.makedirs(output_path)


	# 检查data.json文件是否存在，如果不存在则创建空的json文件
	if not os.path.exists(data_path):
		with open(data_path, "w") as f:
			json.dump({}, f)
