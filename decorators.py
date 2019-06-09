# https://github.com/CoreyMSchafer/code_snippets/blob/master/Decorators/decorators.py
# https://www.youtube.com/watch?v=FsAPt_9Bf3U

import logging
import time

from functools import wraps


def my_logger(orig_func):
    logging.basicConfig(
        filename='{}.log'.format(orig_func.__name__), level=logging.INFO
    )

    @wraps(orig_func)  # this is needed to keep the name of the original func
    def wrapper(*args, **kwargs):
        logging.info(
            'Ran with args: {}, and kwargs: {}'.format(args, kwargs)
        )
        return orig_func(*args, **kwargs)
    return wrapper


def my_timer(orig_func):
    @wraps(orig_func)  # this is needed to keep the name of the original func
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time() - t1
        print('{} ran in: {} seconds'.format(orig_func.__name__, t2))
        return result
    return wrapper


@my_logger
@my_timer
def display_info(name, age):
    time.sleep(1)
    print('display_info ran with arguments ({}, {})'.format(name, age))


def main():
    display_info('Phil', '29')
    display_info('Erin', '29')


if __name__ == "__main__":
    main()

