"""
Logger (via logging)
"""
import logging


#=======================================================================================================================
def get_logger(name: str, console: bool = False) -> logging.Logger:
    """
    Logger by logging

    :param name: Logger name (Ex: 'TEST')
    :param console: Console output (default = False)
    :return: logging.Logger
    """
    # 1.Logger
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # 2.Handler
    handler = logging.StreamHandler()
    handler.setLevel(logging.DEBUG)

    # 3.Formatter
    formatter = logging.Formatter('%(asctime)s | %(name)s | %(levelname)s | %(message)s')

    # 4.ADD
    handler.setFormatter(formatter)

    if console:
        logger.addHandler(handler)

    return logger


#=======================================================================================================================
