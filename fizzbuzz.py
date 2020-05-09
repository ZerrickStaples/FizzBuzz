from helpers import fizzbuzz

print("Welcome to Fizzbuzz! ")

app_status = ''

while app_status.lower() != 'q':
    num = input("Please input a number to pass through the FizzBuzz function: ")
    print(fizzbuzz(int(num)))
    app_status = input(
        "Enter Q to quit. Press enter to pass another number through the function: ")
