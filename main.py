from src.lib.data_process import process_data
from src.lib.ui import create_ui
from src.lib.folder_init import init_folder
from src.common.util import AppConfig

if __name__ == "__main__":
    # 调用初始化函数
    AppConfig.initialize()

    def on_loading():
        init_folder()
        process_data()

    create_ui(on_loading)
