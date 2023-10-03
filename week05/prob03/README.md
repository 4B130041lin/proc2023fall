**Problem 3: Generating a Numbering Matrix**

You are assigned the task of developing a Python script that generates a numerical matrix based on two user-provided integers, R and C. This matrix should be printed in a particular format. To successfully accomplish this assignment, it is essential to employ the `if __name__ == "__main__":` structure and create a primary function. 

`Please note that you are not allowed to use lists or matrices to solve this problem; instead, all numbers must be printed directly.``

*Input:*

The user will input two integers, R and C, where:
- R represents the number of rows in the matrix.
- C represents the number of columns in the matrix.

*Output:*

Your script should generate and print a numbering matrix with the following characteristics:
- The matrix should have R rows and C columns.
- The numbers in the matrix should start from 1 and increment by 1 for each cell, filling each column from left to right and moving to the next column when a column is filled.
- The numbers should be separated by spaces.

*Testing in the Command Prompt:*
```
[prob03]$ python main.py 
4 5
1 5 9 13 17 
2 6 10 14 18 
3 7 11 15 19 
4 8 12 16 20 

[prob03]$ python main.py 
2 6
1 3 5 7 9 11 
2 4 6 8 10 12 
```

*Testing with Input/Output Redirection:*
```
[prob03]$ echo 4 5 | python main.py 
1 5 9 13 17 
2 6 10 14 18 
3 7 11 15 19 
4 8 12 16 20 

[prob03]$ echo 11 13 | python main.py 
   1  12  23  34  45  56  67  78  89 100 111 122 133
   2  13  24  35  46  57  68  79  90 101 112 123 134
   3  14  25  36  47  58  69  80  91 102 113 124 135
   4  15  26  37  48  59  70  81  92 103 114 125 136
   5  16  27  38  49  60  71  82  93 104 115 126 137
   6  17  28  39  50  61  72  83  94 105 116 127 138
   7  18  29  40  51  62  73  84  95 106 117 128 139
   8  19  30  41  52  63  74  85  96 107 118 129 140
   9  20  31  42  53  64  75  86  97 108 119 130 141
  10  21  32  43  54  65  76  87  98 109 120 131 142
  11  22  33  44  55  66  77  88  99 110 121 132 143
```

