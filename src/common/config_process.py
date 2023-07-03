
class ConfigProcess:
    def __init__(self, config_path):
        self.config_path = config_path

    def save_config(self, key, value):
        configs = self.get_all_configs()
        configs[key] = value

        with open(self.config_path, 'w') as f:
            for config_key, config_value in configs.items():
                f.write(f'{config_key}={config_value}\n')

    def read_config(self, key):
        with open(self.config_path, 'r') as f:
            lines = f.readlines()
            for line in lines:
                line = line.strip()
                if line:
                    config_key, config_value = line.split('=')
                    if config_key.strip() == key:
                        return config_value.strip()
        return None

    def get_all_configs(self):
        configs = {}
        with open(self.config_path, 'r') as f:
            lines = f.readlines()
            for line in lines:
                line = line.strip()
                if line:
                    config_key, config_value = line.split('=')
                    configs[config_key.strip()] = config_value.strip()
        return configs

    def has_key(self, key):
        config_value = self.read_config(key)
        return config_value is not None and config_value != ""
