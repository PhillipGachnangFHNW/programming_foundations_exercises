def my_min(numbers):
    min = numbers[0]
    for num in numbers[1:]:
        if num < min:
            min = num

    return min

def min_sorted(l):
    l = sorted(l)
    return l[0]

numbers = [-10001, -100, 3, 6, 2, -19, 0, 3, -40]

print(min_sorted(numbers))