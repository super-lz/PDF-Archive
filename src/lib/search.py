from src.common.json_process import JsonProcess
from src.common.util import data_path

# 这里会返回论文名称和在文章中匹配到的第一条内容
def search(keywords):
    json_process = JsonProcess(data_path)
    res = json_process.fuzzy_search(keywords)
    return res
