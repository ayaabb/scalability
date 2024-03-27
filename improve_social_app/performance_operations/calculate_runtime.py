import time


def calculate_runtime(func_, *parameters):
    start_time = time.perf_counter()
    func_(*parameters)
    end_time = time.perf_counter()
    total_time = round(end_time - start_time, 2)
    return total_time


