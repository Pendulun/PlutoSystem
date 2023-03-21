class InvalidConfigError(Exception):
    def __init__(self, config_option_key, err_msg):
        super().__init__(
            "invalid value for flag '{}': {}".format(
                config_option_key, err_msg,
            )
        )    

    def __init__(self, err_msg):
        super().__init__("invalid configuration: {err_msg}")
