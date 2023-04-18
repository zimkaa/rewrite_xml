from time import perf_counter
from typing import Any
from typing import Callable

from loguru import logger


def my_timer(func: Callable) -> Callable:
    def wrapper(*args, **kwargs) -> Any:
        start = perf_counter()
        result = func(*args, **kwargs)
        stop = perf_counter() - start
        logger.info(f"Execution time {stop}")
        return result

    return wrapper
