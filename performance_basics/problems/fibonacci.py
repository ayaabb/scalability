from results_operations.calculate_runtime import calculate_runtime


def fibonacci_slow_solution(n):
    if n <= 1:
        return n
    else:
        return fibonacci_slow_solution(n - 1) + fibonacci_slow_solution(n - 2)


def fibonacci_fast_solution(n, fib_dict):
    if n in fib_dict:
        return fib_dict[n]
    if n <= 1:
        return n
    fib_dict[n] = fibonacci_fast_solution(n - 1, fib_dict) + fibonacci_fast_solution(n - 2, fib_dict)
    return fib_dict[n]


def calculate_fibo_results():
    nums = [(x * 3) + 10 for x in range(1, 11)]
    results_slow = []
    results_fast = []
    fib_dict = {}
    for num in nums:
        result_slow = calculate_runtime(fibonacci_slow_solution, num)
        result_fast = calculate_runtime(fibonacci_fast_solution, num, fib_dict)
        results_slow.append(result_slow)
        results_fast.append(result_fast)
    return nums,results_slow, results_fast
