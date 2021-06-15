from time import perf_counter
from loguru import logger


def my_timer(func):
    def wrapper(*args, **kwargs):
        start = perf_counter()
        result = func(*args, **kwargs)
        stop = perf_counter() - start
        logger.info(f"Execution time {stop}")
        return result
    return wrapper
