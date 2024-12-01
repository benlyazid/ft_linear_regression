from utils import read_theta_from_csv

def main ():
    theta_0, theta_1 = read_theta_from_csv('thetas.csv')
    #? read miles from user
    km = float(input('Enter the number of Km: '))
    #? calculate the price
    price = theta_0 + theta_1 * km
    print(f'The estimated price for {km} miles is {price}')

if __name__ == '__main__':
    main()