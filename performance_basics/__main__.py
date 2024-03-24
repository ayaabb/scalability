from problems.fibonacci import calculate_fibo_results
from problems.search_element import calculate_search_results
from problems.word_occurrences import calculate_word_occurences_results
from results_operations.results_plot import draw_results
from results_operations.write_results_to_file import write_results


def main():
    # fibonacci
    nums, fib_results_slow, fib_results_fast = calculate_fibo_results()
    draw_results(nums, fib_results_slow, fib_results_fast, 'fibonacci')
    values_info = "n     ,   slow solution Time (s)  ,   fast solution Time (s) "
    write_results("results_files/fibonacci_problem.txt", [nums, fib_results_slow, fib_results_fast], values_info)

    # search
    sizes, slow_results, fast_results = calculate_search_results()
    draw_results(sizes, slow_results, fast_results, "search")
    values_info = "array size ,   slow solution Time (s)  ,   fast solution Time (s) "
    write_results("results_files/search_problem.txt", [sizes, slow_results, fast_results], values_info)

    # count occurrences
    sizes, slow_results, fast_results = calculate_word_occurences_results()
    draw_results(sizes, slow_results, fast_results, "count occurrences")
    values_info = "number of words ,   slow solution Time (s)  ,   fast solution Time (s) "
    write_results("results_files/count_occurrences_problem.txt", [sizes, slow_results, fast_results],values_info)


if __name__ == "__main__":
    main()
