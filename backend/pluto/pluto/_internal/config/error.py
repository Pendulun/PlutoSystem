class InvalidConfigError(Exception):
    def __init__(self, err_msg):
        super().__init__("invalid configuration: {err_msg}")
