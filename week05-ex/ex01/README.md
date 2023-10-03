**Exercise 1: Divisibility Checker in Python**

Develop a Python script named "main.py" that takes a sequence of integers from the user in a single line, with values separated by spaces. The objective is to identify and display the numbers that are divisible by either 3 or 7 while maintaining their original order. In case there are no such divisible numbers, the program should output "None" as the result. Please note that you should not modify "testing.pyc" for successful validation, even if you solve the problem.

*Testing in the Command Prompt:*
```
$ echo 34 45 22 32 23 58 48 28 74 4 53 49 19 74 24 | python main.py 
45 48 28 49 24
```

*Testing with Input/Output Redirection:*
```
cat data.txt | python main.py 
28 7 39 14 49 48 93 15 69
```

*Testing with testing script:*
```
$ python testing.py 
Input: 17 1 28 67 7 19 4 39 14 58 92 37 4 50
Input: 94 49 1 48 93 100 58 15 10 69 26
Input: 19 18 26 61 95 62 96
Input: 34 45 22 32 23 58 48 28 74 4 53 49 19 74 24
Input: 13 43 78 96 74
Input: 29 43 53 52 14 44 95
Input: 54 86 11 29 71 50 13 5 62 86 30 25
Input: 38 50 100 75 39
Input: 17 20 85 98 53 3 92 99 24 28 96 9
Input: 93 93 32 87 81 23 17 41 91 83 67 90 37
.
----------------------------------------------------------------------
Ran 1 test in 0.269s

OK
```
