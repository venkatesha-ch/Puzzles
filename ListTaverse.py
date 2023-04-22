"""
Given a list containing [[1, 2, 3], [4, 5], 7, [8], [9, 10, 11], [12, 13]]. Print each numbers in lines.

Here the normal 2d array traversel wont work. Observe closely the item at position 3 is not a list(but item 4 is a list).
So to solve this we have to explicitly check the type of each row and print.

"""

a = [[1, 2, 3], [4, 5], 7, [8], [9, 10, 11], [12, 13]]
for row in a:
    if type(row) == list:
        for col in row:
            print(col, end="\n")
    else:
        print(row)
        
        
"""
OUTPUT:
1
2
3
4
5
7
8
9
10
11
12
13
"""
