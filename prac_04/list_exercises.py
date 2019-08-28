numbers = []
number_sum = 0

for i in range(5):
    number = int(input("Number :"))
    numbers.append(number)
    number_sum += number

num_ave = number_sum / 5

print("The first number is {} \n".format(numbers[0]),
      "The last number is {}\n".format(numbers[-1]),
      "The smallest number is {}\n".format(min(numbers)),
      "The largest number is {}\n".format(max(numbers)),
      "The average of the numbers is {:.0f}".format(num_ave))


usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

user_input = input("Please enter your username")
if user_input in usernames:
    print("Access Granted")
else:
    print("Access Granted")