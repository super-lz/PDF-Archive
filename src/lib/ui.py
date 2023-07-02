import tkinter as tk
from tkinter import ttk
import os
import sys
import subprocess

from src.common.util import input_path, pdf_suffix
from src.lib.search import search as search_res
from src.lib.data_process import process_data


result_list = None
keyword = ""


def search(keywords):
    process_data()
    return search_res(keywords)


def render_results(results):
    # 清空结果列表
    result_list.delete(*result_list.get_children())

    # 将搜索结果添加到结果列表中
    for i, result in enumerate(results, start=1):
        name = result['name']
        sentence = result['sentence']
        path = os.path.join(input_path, result['name'] + pdf_suffix)
        item_text = f"{i}. {name}"
        result_list.insert('', 'end', values=(item_text, sentence, path))


def open_file(event):
    item = result_list.focus()
    path = result_list.item(item)['values'][2]

    if sys.platform.startswith('win'):
        subprocess.Popen(["start", path], shell=True)
    elif sys.platform.startswith('darwin'):
        subprocess.Popen(["open", path])
    else:
        raise Exception("Unsupported platform")


def create_ui():
    def on_search():
        global keyword
        keyword = entry.get()
        results = search(keyword)
        render_results(results)

    def on_entry_click(event):
        if entry.get() == "请输入关键词句（最多显示15条结果）":
            entry.delete(0, tk.END)

    def on_entry_leave(event):
        if entry.get() == "":
            entry.insert(tk.END, "请输入关键词句（最多显示15条结果）")

    global result_list

    root = tk.Tk()
    root.title("搜索界面")

    # 设置初始大小为800宽400高
    root.geometry("800x400")

    # 输入框和搜索按钮放在同一行
    input_frame = tk.Frame(root)
    input_frame.pack(pady=10)

    entry = tk.Entry(input_frame, width=40, font=("Arial", 14))
    entry.insert(tk.END, "请输入关键词句（最多显示15条结果）")
    entry.bind("<FocusIn>", on_entry_click)
    entry.bind("<FocusOut>", on_entry_leave)
    entry.pack(side=tk.LEFT)

    search_button = tk.Button(input_frame, text="搜索",
                              font=("Arial", 14), command=on_search)
    search_button.pack(side=tk.LEFT, padx=10)

    # 设置结果区域与整个界面的间距为20
    result_frame = tk.Frame(root)
    result_frame.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)

    scrollbar = tk.Scrollbar(result_frame)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    result_list = ttk.Treeview(result_frame, columns=(
        "name", "sentence", "path"), show="headings", selectmode="browse")
    result_list.column("name", width=100, anchor="w")
    result_list.heading("name", text="Name")
    result_list.column("sentence", width=400, anchor="w")
    result_list.heading("sentence", text="Sentence")
    result_list.column("path", width=0, stretch=tk.NO)
    result_list.heading("path", text="Path")
    result_list.pack(fill=tk.BOTH, expand=True)

    # 绑定打开文件事件
    result_list.bind("<Double-Button-1>", open_file)

    result_list.configure(yscrollcommand=scrollbar.set)
    scrollbar.configure(command=result_list.yview)

    root.mainloop()
