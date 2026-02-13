def absolute_difference(a, b):
    c = a - b

    if c < 0:
        c *= -1

    return int(c)


def count_vowels(s):
    vowels = ["a", "e", "i", "o", "u", "y"]
    count = 0
    for letter in s:
        if letter.lower() in vowels:
            count += 1
    return count


def average(numbers):
    numbers_sum = 0
    if len(numbers) == 0:
        return 0.0
    for num in numbers:
        numbers_sum += num
    ave = float(numbers_sum) / (len(numbers))
    ave = round(ave, 2)
    return ave


def is_even(num):
    if num % 2 == 0:
        return True
    return False


def classify_grade(grade):
    if grade >= 90:
        return "A"
    elif grade >= 80:
        return "B"
    elif grade >= 70:
        return "C"
    elif grade >= 60:
        return "D"
    else:
        return "F"
