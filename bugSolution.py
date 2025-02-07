def calculate_average(numbers):
    if not numbers:
        return 0
    numeric_numbers = [num for num in numbers if isinstance(num, (int, float))]
    if not numeric_numbers:
        return 0  # Handle list with only non-numeric values
    return sum(numeric_numbers) / len(numeric_numbers)

my_list = []
result = calculate_average(my_list)
print(result)  # Output: 0

my_list = [1, 2, 3, 4, 5]
result = calculate_average(my_list)
print(result)  # Output: 3.0

my_list = [1, 2, 3, 4, 'a']
result = calculate_average(my_list)
print(result)  # Output: 2.5