import os

# change the value for a different result
num = os.getenv('FACTORIAL_NUMBER', 7)

factorial = 1

# check if the number is negative, positive or zero
if num < 0:
    raise RuntimeError('Sorry, factorial does not exist for negative numbers')
elif num == 0:
    print('The factorial of 0 is 1')
else:
    for i in range(1, num + 1):
        factorial = factorial * i
    print(f'The factorial of {num} is {factorial}')