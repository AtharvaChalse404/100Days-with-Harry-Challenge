# atharva.py

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

def print_prime_numbers():
    for i in range(1, 200, 2):
        if is_prime(i):
            print(i)

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def is_even(n):
    if n % 2 == 0 and n > 1:
        return 'Is Even'
    else:
        return 'Is Odd'

# This block will only run if the script is executed directly
if __name__ == "__main__":
    # Example usage when executed directly
    user_input = int(input('Please Enter a Number: '))
    result = factorial(user_input)
    print(f"The factorial of {user_input} is: {result}")

    number = int(input('Please Enter a Number: '))
    result = is_even(number)
    print(result)
