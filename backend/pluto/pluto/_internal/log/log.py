import logging

FORMATTER = logging.Formatter("[%(levelname)s] %(asctime)s %(message)s")

ALL_LOGGING_LEVELS = {
    "DEBUG": logging.DEBUG,
    "INFO": logging.INFO,
    "WARNING": logging.WARNING,
    "ERROR": logging.ERROR,
    "CRITICAL": logging.CRITICAL,
}
LOGGING_LEVEL = logging.CRITICAL

all_loggers_map: dict = {}


def set_level(log_level_name):
    if log_level_name not in ALL_LOGGING_LEVELS:
        raise ValueError(
            f"got invalid log level '{log_level_name}'. "
            + "Should be one of {list(ALL_LOGGING_LEVELS.keys())}"
        )

    global LOGGING_LEVEL
    global all_loggers_map

    log_level = ALL_LOGGING_LEVELS[log_level_name]

    LOGGING_LEVEL = log_level
    for logger in all_loggers_map:
        all_loggers_map[logger].setLevel(log_level)


def stream_handler():
    h = logging.StreamHandler()
    h.setFormatter(FORMATTER)
    return h


def logger():
    global all_loggers_map

    logger_name = "plutosystem"

    if all_loggers_map.get(logger_name):
        return all_loggers_map.get(logger_name)
    else:
        logger = logging.getLogger(logger_name)
        for h in logger.handlers:
            logger.removeHandler(h)
        logger.propagate = False
        logger.setLevel(LOGGING_LEVEL)
        logger.addHandler(stream_handler())

        all_loggers_map[logger_name] = logger
        return logger
