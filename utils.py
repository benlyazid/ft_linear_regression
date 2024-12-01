import  matplotlib.pyplot as plt

def read_data(file_path):
    '''
    Read data from a csv file
    Args:
        - file_path: str, path to the csv file
    Returns:
        list of lists: list of lists containing the data from the csv file :
        EX: [[km, price][km, price]...]
    '''
    try:
        print('\033[92m' + f'1. Start reading data from [{file_path}]' + '\033[0m')
        with open(file_path, 'r') as file:
            data = file.read()
            data = data.split('\n')
            data = [line.split(',') for line in data]
            data = data[1:]
            data = [[float(line[0]), float(line[1])] for line in data if len(line) == 2]
        print('\033[92m' + f'Data read successfully from [{file_path}]' + '\033[0m\n\n')
        return data
    except Exception as e:
        print('\033[91m' + f'Error reading data from [{file_path}]: {e}' + '\033[0m')
        exit()

def plot_data_and_error(data, theta_0, theta_1, min_x, max_x, error):
    '''
    Plot the data and the error
    Args:
        - data: list of lists, data to plot [km, price]
        - theta_0: float, intercept of the regression line
        - theta_1: float, slope of the regression line
        - min_x: float, minimum value of x
        - max_x: float, maximum value of x
        - error: list of lists, error to plot [epoch, error] (mean squared error)
    Returns:
        None
    '''
    try:
        print('\033[92m' + '3. Start plotting data and error' + '\033[0m')
        fig, ax = plt.subplots(1, 2, figsize=(12, 5))
        ax[0].scatter([line[0] for line in data], [line[1] for line in data])
        ax[0].set_xlabel('Km')
        ax[0].set_ylabel('Price')
        ax[0].set_title('Price vs Km')
        x = [min_x, max_x]
        y = [theta_0 + theta_1 * min_x, theta_0 + theta_1 * max_x]
        ax[0].plot(x, y, color='red')

        ax[1].scatter([line[0] for line in error], [line[1] for line in error])
        ax[1].set_xlabel('epoch')
        ax[1].set_ylabel('Mean Squared Error')
        ax[1].set_title('Error vs Iteration')
        plt.show()
        print('\033[92m' + 'Data and error plotted successfully' + '\033[0m')
    except Exception as e:
        print('\033[91m' + f'Error plotting data and error: {e}' + '\033[0m')
        exit()

def save_theta_to_csv(theta_0, theta_1, file_path):
    '''
    Save the regression parameters to a csv file
    Args:
        - theta_0: float, intercept of the regression line
        - theta_1: float, slope of the regression line
    Returns:
        None
    '''
    try:
        print('\033[92m' + '3. Start saving thetas to csv' + '\033[0m')
        data  = 'theta_0,theta_1\n'
        data += f'{theta_0},{theta_1}'
        with open('thetas.csv', 'w') as file:
            file.write(data)
        print('\033[92m' + 'Thetas saved successfully\n\n' + '\033[0m')
    except Exception as e:
        print('\033[91m' + f'Error saving thetas to csv: {e}' + '\033[0m')
        exit()


def read_theta_from_csv(file_path):
    '''
    Read the regression parameters from a csv file
    Args:
        - file_path: str, path to the csv file
    Returns:
        - tuple: tuple containing the regression parameters (theta_0, theta_1)
    '''
    try:
        print('\033[92m' + f'Start reading thetas from [{file_path}]' + '\033[0m')
        with open(file_path, 'r') as file:
            data = file.read()
            data = data.split('\n')
            data = data[1].split(',')
            theta_0 = float(data[0])
            theta_1 = float(data[1])
        print('\033[92m' + f'Thetas read successfully from [{file_path}]' + '\033[0m')
        return theta_0, theta_1
    except Exception as e:
        return 0, 0