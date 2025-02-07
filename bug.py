def calculate_average(numbers):
    if not numbers:  # Handle empty list
        return 0
    return sum(numbers) / len(numbers)

my_list = []
result = calculate_average(my_list)
print(result)  # Output: 0

my_list = [1, 2, 3, 4, 5]
result = calculate_average(my_list)
print(result)  # Output: 3.0

my_list = [1,2,3,4,'a']
result = calculate_average(my_list) # This will throw an error
print(result)