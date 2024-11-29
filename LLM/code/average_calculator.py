# filename: average_calculator.py

def calculate_average(numbers):
    """
    Calculate the average of a list of numbers.

    Args:
        numbers (list): A list of numbers.

    Returns:
        float: The average of the numbers in the list.
    """
    return sum(numbers) / len(numbers)

numbers = [1, 2, 3, 4, 5]
average = calculate_average(numbers)
print(average)  # Outputs: 3.0