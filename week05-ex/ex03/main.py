#! /usr/bin/env python3

# exercise: 03

input_numbers = input()
numbers = [int(num) for num in input_numbers.split()]
divisible_by_3_or_7 = [str(num) for num in numbers if num % 5 == 0 or num % 7 == 0]
if divisible_by_3_or_7:
    print(" ".join(divisible_by_3_or_7))
else:
    print("None")
