import colorlog

from logging import Logger

logger: Logger


def init_logger():
    global logger
    handler = colorlog.StreamHandler()
    handler.setFormatter(colorlog.ColoredFormatter(
        '[%(log_color)s%(asctime)s: %(levelname)s/%(processName)s:%(threadName)s] %(message)s'))
    logger = colorlog.getLogger(__name__)
    logger.propagate = False
    logger.addHandler(handler)
    logger.setLevel(colorlog.colorlog.logging.INFO)


init_logger()
