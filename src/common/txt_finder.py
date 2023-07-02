import os
import json
import concurrent.futures

class TxtFinder:
    def __init__(self, file_paths):
        self.file_paths = file_paths

    def _search_sentence_in_file(self, file_path, sentence):
        file_results = []
        with open(file_path, 'r') as file:
            for line in file:
                if sentence in line:
                    file_results.append(line.strip())
        return {'file': file_path, 'matches': file_results}

    def search_sentence(self, sentence):
        results = []
        with concurrent.futures.ThreadPoolExecutor() as executor:
            # 提交每个文件的查找任务给线程池
            futures = [executor.submit(self._search_sentence_in_file, file_path, sentence) for file_path in self.file_paths]

            # 获取任务的结果
            for future in concurrent.futures.as_completed(futures):
                result = future.result()
                results.append(result)

        # 按文件的修改时间排序结果
        sorted_results = sorted(results, key=lambda x: os.path.getmtime(x['file']))

        # 输出结果为JSON
        output_json = json.dumps(sorted_results, indent=4)
        return output_json

