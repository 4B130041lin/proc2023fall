**Problem 2: Recursion-Based Exponentiation**

In this challenge, your objective is to calculate the result of raising a positive real number, denoted as "a," to the power of a non-negative integer, denoted as "n." However, you are prohibited from using loops, the ** operator, or the built-in math.pow() function. Instead, you must employ recursion and adhere to the following mathematical relation: an = a * a^(n-1).

To achieve this, create a file named "main.py" and implement a recursive function called "power(a, n)." Your task is to ensure that this function accurately computes the desired result and prints it.

*Testing in the Command Prompt:*
```
[prob02]$ python main.py 
3
5
243
```

*Testing with Input/Output Redirection:*
```
[prob02]$ cat data.txt 
2
16
[prob02]$ cat data.txt | python main.py 
65536
```

*Testing with testing script:*
```
[prob02]$ python testing.py 
 13  28
 20  24
  8   4
 27   8
...
... (truncated for brevity)
...
 10  15
 22  23
 27   4
 26   6
 13   4
.
----------------------------------------------------------------------
Ran 1 test in 2.346s

OK
```
