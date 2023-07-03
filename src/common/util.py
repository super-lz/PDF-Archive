import os
import sys
from src.common.config_process import ConfigProcess

class AppConfig:
    origin_dir_key = 'origin_dir'
    pdf_suffix = '.pdf'
    txt_suffix = '.txt'

    main_path = None
    config_path = None
    _default_input_path = None
    output_path = None
    data_path = None

    @classmethod
    def initialize(cls):
        cls.main_path = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
        if getattr(sys, 'frozen', False):
            cls.main_path = os.path.abspath(os.path.dirname(sys.executable))
        cls.config_path = os.path.abspath(os.path.join(cls.main_path, '.config'))
        if not os.path.exists(cls.config_path):
            with open(cls.config_path, "w") as f:
                f.write('')
        cls._default_input_path = os.path.abspath(os.path.join(cls.main_path, 'origin'))
        cls.output_path = os.path.abspath(os.path.join(cls.main_path, 'source'))
        cls.data_path = os.path.abspath(os.path.join(cls.main_path, 'data.json'))

    @classmethod
    def get_input_path(cls):
        config_processor = ConfigProcess(cls.config_path)
        return os.path.abspath(config_processor.read_config(cls.origin_dir_key)
                               if config_processor.has_key(cls.origin_dir_key) else cls._default_input_path)