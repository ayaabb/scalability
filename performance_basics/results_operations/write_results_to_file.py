def write_results(file_name, results,values_info):
    with open(file_name, 'w') as file:
        file.write(values_info+'\n')
        for n, time_recursive, time_iterative in zip(*results):
            file.write(f"    {n}        ,   {time_recursive}         ,   {time_iterative}\n")
