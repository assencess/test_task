#!/usr/bin/env python3
def get_sum_mul(number):
    '''
    Function returns two vars. First is sum of numbers,
    second is production of number.
    '''
    return (number + number), (number ** 2)

if __name__ == "__main__":
    number = input("Enter a number, please: ")
    amount, product = get_sum_mul(int(number))
    print("Amount of {0} is {1}\nProduction of {0} is {2}" \
        .format(number, amount, product))