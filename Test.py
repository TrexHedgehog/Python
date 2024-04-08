def check_even_odd(number):
    """
    Check if a given number is even or odd.

    Args:
        number (int): The number to be checked.

    Returns:
        str: 'Even' if the number is even, 'Odd' otherwise.
    """
    if number % 2 == 0:
        return 'Even'
    else:
        return 'Odd'

def main():
    # Input the number from the user
    number = int(input("Enter a number: "))

    # Check if the number is even or odd
    result = check_even_odd(number)

    # Print the result
    print("The number is", result)

if __name__ == "__main__":
    main()
