from fizzbuzz import fizzbuzz

def test_return_number():
    assert fizzbuzz(1) == 1

def test_return_fizz():
    assert fizzbuzz(3) == "Fizz"

def test_return_buzz():
    assert fizzbuzz(5) == "Buzz"

def test_return_fizzbuzz():
    assert fizzbuzz(15) == "FizzBuzz"