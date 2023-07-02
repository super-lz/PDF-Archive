from src.lib.data_process import process_data
from src.lib.ui import create_ui
from src.lib.folder_init import init_folder


if __name__ =="__main__":
    init_folder()

    process_data()

    create_ui()
