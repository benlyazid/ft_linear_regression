from utils import read_data, plot_data_and_error, save_theta_to_csv
from tqdm import tqdm

class Train():
    def __init__(self, debug=True, learning_rate=0.01, epoch=100000, file_path='data.csv'):
        self.data = read_data(file_path)
        self.original_data = self.data
        self.learning_rate = learning_rate
        self.epoch = epoch
        self.theta_0 = 0
        self.theta_1 = 0
        self.min_x = min([line[0] for line in self.data])
        self.max_x = max([line[0] for line in self.data])
        self.range_x = self.max_x - self.min_x
        self.min_y = min([line[1] for line in self.data])
        self.max_y = max([line[1] for line in self.data])
        self.range_y = self.max_y - self.min_y
        self.data_length = len(self.data)
        self.debug = debug
        self.errors = []

    def train(self):
        print('\033[92m' + '2. Start training' + '\033[0m')
        last_mean_squared_error = 0
        self.normalize_data()
        for i in tqdm(range(self.epoch)):
            self.update_theta_0_and_theta_1()
            mean_squared_error = self.calculate_mean_squared_error()
            self.errors.append([i, mean_squared_error])
            if i % 1000 == 0 and self.debug:
                print(f'Epoch: {i} Theta_0: {self.theta_0} Theta_1: {self.theta_1}')
                print('\033[93m' + f'Mean Squared Error: {mean_squared_error}' + '\033[0m')
        print('\033[92m' + 'Training completed with the following results' + '\033[0m]\n\n')
        print(f'Theta_0: {self.theta_0} Theta_1: {self.theta_1}')
        self.theta_0, self.theta_1 = self.scale_parameters_to_original(self.theta_0, self.theta_1)

        save_theta_to_csv(self.theta_0, self.theta_1, 'theta.csv')


    def predict(self, x):
        '''
            Predict the price of a car given the mileage
        '''
        predicted_price = self.theta_0 + self.theta_1 * x
        return predicted_price

    def calculate_gradient_descent(self):
        '''
            Calculate the gradient descent for theta_0 and theta_1
        '''
        sum_theta_0 = 0
        sum_theta_1 = 0
        for i in range(len(self.data)):
            sum_theta_0 += self.predict(self.data[i][0]) - self.data[i][1]
            sum_theta_1 += (self.predict(self.data[i][0]) - self.data[i][1]) * self.data[i][0]
        return sum_theta_0, sum_theta_1
    

    def update_theta_0_and_theta_1(self):
        '''
            Update theta_0 and theta_1 using gradient descent
        '''
        loss = self.calculate_gradient_descent()
        self.theta_0 -= (self.learning_rate / len(self.data)) * loss[0]
        self.theta_1 -= (self.learning_rate / len(self.data)) * loss[1]

    def calculate_mean_squared_error(self):
        sum_error = 0
        for i in  range(self.data_length):
            sum_error += (self.predict(self.data[i][0]) - self.data[i][1]) ** 2
        return sum_error / self.data_length


    def normalize_data(self):
        '''
            Normalize the data to be between 0 and 1
        '''
        self.data = [[(line[0] - self.min_x) / self.range_x, (line[1] - self.min_y) / self.range_y] for line in self.data]

    def scale_parameters_to_original(self, theta_0, theta_1):
        """
        Scale regression parameters from standardized data back to the original scale.
        
        Args:
        - theta_0 (float): Intercept from the standardized regression model.
        - theta_1 (float): Slope from the standardized regression model.
        
        Returns:
        - (float, float): Intercept and slope scaled to the original data.
        """
        #? Scale the slope
        theta_1_original = theta_1 * self.range_y / self.range_x

        #? Scale the intercept
        theta_0_original = self.min_y + theta_0 * self.range_y - theta_1 * self.min_x * self.range_y / self.range_x

        return theta_0_original, theta_1_original

if __name__ == '__main__':
    
    train = Train(debug=False, learning_rate=0.01, epoch=10000, file_path='data.csv')
    train.train()
    plot_data_and_error(train.original_data, train.theta_0, train.theta_1, train.min_x, train.max_x, train.errors)