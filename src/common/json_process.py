import json
import os
import re


class JsonProcess:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = self._load_data()

    def _load_data(self):
        if os.path.getsize(self.file_path) == 0:
            data = []
        else:
            with open(self.file_path, 'r') as file:
                json_data = json.load(file)
                data = json_data.get("data", [])
        return data

    def _save_data(self):
        json_data = {"data": self.data}
        with open(self.file_path, 'w') as file:
            json.dump(json_data, file, indent=4)

    def object_exists(self, name):
        for item in self.data:
            if name in item['name']:
                return True
        return False

    def delete_object(self, name):
        for item in self.data:
            if item['name'] == name:
                self.data.remove(item)
                break

    def add_object(self, file_name, file_path):
        with open(file_path, 'r') as file:
            content = file.read()
        new_object = {'name': file_name, 'content': content}
        self.data.append(new_object)

    def save_data(self):
        self._save_data()

    def fuzzy_search(self, keyword):
        keyword = keyword.replace(" ", "")
        results = []
        pattern = re.compile(re.escape(keyword), re.IGNORECASE)
        for item in self.data:
            name = item['name']
            content = item['content']
            name_match = pattern.search(name.replace(" ", ""))
            content_match = pattern.search(content.replace(" ", ""))
            if name_match and content_match:
                content_start_index = max(content_match.start() - 20, 0)
                content_end_index = min(content_match.end() + 20, len(content))
                sentence = content[content_start_index:content_end_index]
            elif content_match:
                content_start_index = max(content_match.start() - 20, 0)
                content_end_index = min(content_match.end() + 20, len(content))
                sentence = content[content_start_index:content_end_index]
            elif name_match:
                name_start_index = max(name_match.start() - 20, 0)
                name_end_index = min(name_match.end() + 20, len(name))
                sentence = name[name_start_index:name_end_index]
            else:
                continue
            result = {'name': name, 'sentence': sentence}
            results.append(result)
            if len(results) >= 15:
                break
        return results
