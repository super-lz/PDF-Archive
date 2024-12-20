from src.common.json_process import JsonProcess
from src.common.util import AppConfig
from src.lib.data_process import process_data
from src.lib.folder_init import init_folder

# 这里会返回论文名称和在文章中匹配到的第一条内容
def search(keywords):
    keywords = keywords.strip()
    if not keywords:
        return []

    init_folder()
    process_data()
    json_process = JsonProcess(AppConfig.data_path)
    res = json_process.fuzzy_search(keywords)
    return res
