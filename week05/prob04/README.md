**Problem 4: Calculate Variance**

Create a Python script that calculates the variance of a list of integers.

Define a function named calculate_variance(numbers) that takes a list of integers as input and returns the variance.

*The variance should be calculated in the following steps:*
- Calculate the mean (average) of the numbers in the list.
- For each number in the list, compute the squared difference between the number and the mean.
- Find the average of these squared differences.
- Return the calculated variance.
- Handle the case when the input list has fewer than 2 elements by returning None.

*The variance of a set of data points is calculated using the following formula:*
```scss
Var(X) = (1/(n-1)) * Σ(Xi - X̄)^2

Where:

- Var(X) is the variance of the data set.
- n is the number of data points.
- Xi represents each individual data point.
- X̄ is the mean (average) of the data points.
```

*Testing in the Command Prompt:*
```
[prob04]$ python main.py 
1 2 3 4 5
2.5

[prob04]$ python main.py 
2 4 6 8 10
10.0
```

*Testing with Input/Output Redirection:*
```
[prob04]$ echo 1 2 3 4 5 6 7 8 9 10 | python main.py 
9.17

[prob04]$ echo 1 3 5 7 9 11 | python main.py 
14.0
```
