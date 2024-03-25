import os


def write_results(file_name, results):
    if not os.path.exists(file_name):
        with open(file_name, 'w') as file:
            file.write(results+'\n')

    else:
        # Open the file in append mode
        with open(file_name, 'a') as file:
            # Write or append content to the file
            file.write(results+"\n")
