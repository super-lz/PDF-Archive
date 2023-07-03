import os
import sys
from src.common.config_process import ConfigProcess


class AppConfig:
    origin_dir_key = 'origin_dir'
    pdf_suffix = '.pdf'
    txt_suffix = '.txt'

    main_path = os.path.join(os.path.dirname(
        os.path.abspath(__file__)), '..', '..')
    if getattr(sys, 'frozen', False):
        main_path = os.path.dirname(sys.executable)
    config_path = os.path.join(main_path, '.config')
    _config_processor = ConfigProcess(config_path)
    default_input_path = os.path.join(main_path, 'origin')
    output_path = os.path.join(main_path, 'source')
    data_path = os.path.join(main_path, 'data.json')

    @classmethod
    def get_input_path(cls):
        return cls._config_processor.read_config(cls.origin_dir_key) if cls._config_processor.has_key(cls.origin_dir_key) else cls.default_input_path
