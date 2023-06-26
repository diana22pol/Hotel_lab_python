from types import FunctionType
from functools import wraps
import logging
from tools.exeptions import RatingError, TotalRoomsError


def logged(exeption: Exception, mode: str = "console"):
    """A decorator that logs exceptions raised by the decorated function.
    Args:
        exception (Exception): The exception class to be logged.
        mode (str, optional): The logging mode. Valid values are "console" or "file".
            Defaults to "console".
            :param mode:
            :param exeption:
    """

    def wrapper(func: FunctionType):
        loger = logging.getLogger(func.__name__)
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        if mode == "console":
            console_handler = logging.StreamHandler()
            console_handler.setFormatter(formatter)
            loger.addHandler(console_handler)
        elif mode == "file":
            file_handler = logging.FileHandler(filename="loged.log")
            file_handler.setFormatter(formatter)
            loger.addHandler(file_handler)
        else:
            raise RatingError|TotalRoomsError

        @wraps(func)
        def inner(*args, **kwargs):
            nonlocal loger
            try:
                return func(*args, **kwargs)
            except exeption as ex:
                loger.error("%s: %s", ex.__class__.__name__, ex)
                raise
            except Exception as ex:
                loger.error("other exception: %s: %s", ex.__class__.__name__, ex)
                raise

        return inner

    return wrapper
