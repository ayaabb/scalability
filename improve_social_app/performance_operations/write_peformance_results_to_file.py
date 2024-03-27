import os


def write_results_to_file(file_name, func, results, before_or_after):
    if not os.path.exists(file_name):
        with open(file_name, 'w') as file:
            info=f"the execution time of '{func}' function {before_or_after} improving = " + str(results) + '\n'
            print(info)
            file.write(info)

    else:
        # Open the file in append mode
        with open(file_name, 'a') as file:
            # Write or append content to the file
            info = f"the execution time of '{func}' function  {before_or_after} improving = " + str(results) + '\n'
            print(info)
            file.write(info)
