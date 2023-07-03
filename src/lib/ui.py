import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import os
import sys
import subprocess

from src.common.util import AppConfig
from src.common.config_process import ConfigProcess
from src.lib.data_process import process_data
from src.lib.search import search
from src.lib.folder_init import init_folder, clear_folder


result_list = None
keyword = ""


def render_results(results):
    # 清空结果列表
    result_list.delete(*result_list.get_children())

    # 将搜索结果添加到结果列表中
    for i, result in enumerate(results, start=1):
        name = result['name']
        sentence = result['sentence']
        path = os.path.join(AppConfig.get_input_path(),
                            result['name'] + AppConfig.pdf_suffix)
        item_text = f"{i}. {name}"
        result_list.insert('', 'end', values=(item_text, sentence, path))


def open_file(event):
    item = result_list.focus()
    path = result_list.item(item)['values'][2]

    if sys.platform.startswith('win'):
        os.startfile(path)
    elif sys.platform.startswith('darwin'):
        subprocess.Popen(["open", path])
    else:
        raise Exception("Unsupported platform")


def create_ui(on_loading):
    def on_select():
        root = tk.Tk()
        root.withdraw()

        # 选择文件夹
        folder_path = filedialog.askdirectory()

        if folder_path:
            # 创建 ConfigProcess 实例，传入元数据文件的路径
            config_processor = ConfigProcess(AppConfig.config_path)

            # 保存文件夹路径到元数据文件中
            config_processor.save_config('origin_dir', folder_path)

            print('文件夹路径已保存到 {} 文件中。'.format(AppConfig.config_path))

            entry.config(state=tk.DISABLED)  # 禁用输入框
            search_button.config(state=tk.DISABLED)  # 禁用搜索按钮
            select_button.config(state=tk.DISABLED)  # 禁用选择文件按钮
            result_list.delete(*result_list.get_children())  # 清空结果列表
            label_loading.pack()  # 显示加载提示信息
            root.update()  # 更新界面，以显示加载提示

            # 清除之前处理得到的数据
            clear_folder()

            # 新建数据文件夹
            init_folder()

            # 重新处理数据
            process_data()

            # 搜索过程
            results = search(keyword)
            render_results(results)

            label_loading.pack_forget()  # 隐藏加载提示信息
            entry.config(state=tk.NORMAL)  # 启用输入框
            search_button.config(state=tk.NORMAL)  # 启用搜索按钮
            select_button.config(state=tk.NORMAL)  # 启用文件选择按钮
        else:
            print('未选择文件夹，路径未保存。')

    def on_search():
        global keyword
        keyword = entry.get()
        entry.config(state=tk.DISABLED)  # 禁用输入框
        search_button.config(state=tk.DISABLED)  # 禁用搜索按钮
        result_list.delete(*result_list.get_children())  # 清空结果列表
        label_loading.pack()  # 显示加载提示信息
        root.update()  # 更新界面，以显示加载提示

        # 搜索过程
        results = search(keyword)
        render_results(results)

        label_loading.pack_forget()  # 隐藏加载提示信息
        entry.config(state=tk.NORMAL)  # 启用输入框
        search_button.config(state=tk.NORMAL)  # 启用搜索按钮

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

    # 显示加载状态
    label = tk.Label(root, text="数据加载需要较长时间，请稍候...")
    label.pack()
    root.update()
    on_loading()
    label.pack_forget()
    root.update()

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

    label_loading = tk.Label(root, text="正在加载，请稍后...")
    label_loading.pack_forget()  # 默认隐藏加载提示信息


    select_frame = tk.Frame(root)
    select_frame.pack(pady=10, padx=10, side=tk.LEFT)

    select_button = tk.Button(select_frame, text="重置文件入口", font=("Arial", 14), command=on_select)
    select_button.pack(anchor='w')

    # 创建标签，设置文本、背景和前景颜色
    label = tk.Label(select_frame, text=AppConfig.get_input_path(), wraplength=root.winfo_width() - 20, state=tk.NORMAL, anchor='w')
    label.pack(fill=tk.BOTH, padx=10, pady=(0, 10), expand=True)
    label.config(height=2)

    root.mainloop()
