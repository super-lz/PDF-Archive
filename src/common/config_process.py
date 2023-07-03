class ConfigProcess:
    def __init__(self, config_path):
        self.config_path = config_path
        self.configs = self.load_configs()

    def save_config(self, key, value):
        self.configs[key] = value

        with open(self.config_path, 'w') as f:
            for config_key, config_value in self.configs.items():
                f.write(f'{config_key}={config_value}\n')

    def read_config(self, key):
        return self.configs.get(key)

    def load_configs(self):
        configs = {}
        with open(self.config_path, 'r') as f:
            lines = f.readlines()
            for line in lines:
                line = line.strip()
                if line:
                    config_key, config_value = line.split('=')
                    configs[config_key.strip()] = config_value.strip()
        return configs

    def has_config(self, key):
        config_value = self.read_config(key)
        return config_value is not None and config_value != ""
