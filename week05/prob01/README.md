**Problem 1: Calculating Distance in 3D Space**

You have been assigned the task of creating a Python program (main.py) capable of computing the distance between two points in three-dimensional space. This challenge will assess your proficiency in applying the Euclidean distance formula to determine distances in a 3D coordinate system. Please note that it is crucial not to make any modifications to the testing.pyc file, as doing so may result in the validation failure of your script.

*Input:*
The input comprises the integer coordinates of two points in three-dimensional space: (x1, y1, z1) and (x2, y2, z2). These coordinates represent the positions of the two points. The following values are the input for the two points:

```
1 2 3
4 5 6
```

*Output:*
Your program should calculate and output the Euclidean distance between the two points. Round the result to two decimal places.

*Formula:*
The Euclidean distance between two points (x1, y1, z1) and (x2, y2, z2) is calculated using the following formula:

```
distance = sqrt((x2 - x1)^2 + (y2 - y1)^2 + (z2 - z1)^2)
```

*Testing in the Command Prompt:*
```
[prob01]$ python main.py 
1 2 3
4 5 6
5.2
```

*Testing with Input/Output Redirection:*
```
[prob01]$ cat data.txt 
-10 3 4
10 -3 -5
[prob01]$ cat data.txt | python main.py 
22.74
```

*Testing with testing script:*
```
[prob01]$ python testing.py 
[5, 0, -6]      [3, -2, 10]    
[-9, 5, -5]     [1, -1, 10]    
[0, 2, 5]       [3, -6, 8]     
[1, 4, 1]       [3, -4, 2]     
...
... (truncated for brevity)
...
[7, 10, -8]     [-10, 5, 5]    
[9, 3, -10]     [5, -9, -8]    
[8, 5, 5]       [-4, 4, -4]    
[-2, 2, 0]      [7, -5, -5]    
[9, -1, -10]    [-6, -3, -8]   
.
----------------------------------------------------------------------
Ran 1 test in 2.372s

OK
```
