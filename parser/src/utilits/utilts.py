import json
import os


def read_html_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()


def save_to_json(data, filename):
    with open(filename, "w", encoding="utf-8") as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)


def make_dir(patch):
    if not os.path.exists(patch):
        os.makedirs(patch)
