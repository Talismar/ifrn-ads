from time import time


def start_time_fun():
    return time()


def end_time_fun(start_time: float):
    return time() - start_time
