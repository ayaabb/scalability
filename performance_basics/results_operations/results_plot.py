import matplotlib.pyplot as plt


def draw_results(x_values, y_values_slow, y_values_fast, func_name):
    plt.scatter(x_values, y_values_slow, label='Slow', color='red')
    plt.scatter(x_values, y_values_fast, label='Fast', color='blue')
    plt.xlabel('Input')
    plt.ylabel('Time')
    plt.title(func_name)
    plt.legend()
    plt.grid(True)
    plt.savefig('results_files/'+func_name + '.png')
    plt.show()

