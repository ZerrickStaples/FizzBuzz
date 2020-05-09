result = ''
def fizzbuzz(num):
    if num % 5 == 0 and num % 3 == 0:
        result = "FizzBuzz"
    elif num % 5 == 0:
        result = "Buzz"
    elif num % 3 == 0:
        result = "Fizz"
    else:
        result = num
    return result