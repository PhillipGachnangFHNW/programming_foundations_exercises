def my_min(numbers):
    min = numbers[0]
    for num in numbers[1:]:
        if num < min:
            min = num
    return min

numbers = [1, 3, 6, 2, -19, 0, 3]

print(my_min(numbers))