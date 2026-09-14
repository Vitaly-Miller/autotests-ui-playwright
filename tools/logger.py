"""
Logger (via logging)
"""
import logging

#=======================================================================================================================
def get_logger(name: str, console: bool = False) -> logging.Logger:
    """
    Создает и настраивает Logger by logging

    :param name: Logger name (Ex: 'TEST')
    :param console: Выводить ли log в консоль (default = False)
    :return: logging.Logger
    """
    # 1.Logger
    logger = logging.getLogger(name)         # Создаем Logger и присваиваем ему динамическое название name (из функции)
    logger.setLevel(logging.DEBUG)           # Уровень (глубина) логирования - DEBUG и выше (все)

    # 2.Handler
    handler = logging.StreamHandler()        # Создаем Handler (обработчик) - StreamHandler для консоли
    handler.setLevel(logging.DEBUG)          # Уровень (глубина) логирования - DEBUG и выше (все)

    # 3.Formatter (формат лога)   |    время   |   имя    |    уровень    |  сообщение |
    formatter = logging.Formatter('%(asctime)s | %(name)s | %(levelname)s | %(message)s')

    # 4.ADD
    handler.setFormatter(formatter)          # Добавляем Handler (обработчик) в Formatter

    if console:                              # Условие, если console=True (default - False)
        logger.addHandler(handler)           # Выводить log в консоль

    return logger


#=======================================================================================================================
