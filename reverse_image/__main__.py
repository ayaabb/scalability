import multi_process
import single_process
from calc_runtime import calculate_runtime
from write_results_to_file import write_results


def main():
    # Example usage
    img_path = 'img1.jpg'
    run_time_single = calculate_runtime(single_process.reverse_image, img_path)
    result_single = f"Single process reverse image run time = {run_time_single}"
    print(result_single)
    run_time_multi = calculate_runtime(multi_process.reverse_image, img_path)
    result_multi = f"Multi process reverse image run time = {run_time_multi}"
    print(result_multi)
    result_file = "result_files/results.txt"
    write_results(result_file, result_single)
    write_results(result_file, result_multi)


if __name__ == '__main__':
    main()
