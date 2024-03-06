num = input('Enter a number (decimal only): ')
# type your code here
position = num.find(".")
num_decimal = num[position + 1:]
dp = len(num_decimal)


# do not change any code beyond this point
print('The number', num, 'has', dp, 'decimal places.')
