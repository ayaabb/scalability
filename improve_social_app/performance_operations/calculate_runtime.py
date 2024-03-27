import time


def calculate_runtime(func_, *parameters):
    """Calculate the runtime of a given function with parameters.
      param :func_ (callable): The function to be executed.
          *parameters: Variable-length arguments to be passed to the function.
      Returns:  float: The total runtime of the function execution in seconds.
      """
    start_time = time.perf_counter()
    func_(*parameters)
    end_time = time.perf_counter()
    total_time = round(end_time - start_time, 2)
    return total_time


