""" 
Task
Sum all the numbers of a given array ( cq. list ), except the highest and the lowest element ( by value, not by index! ).

The highest or lowest element respectively is a single element at each edge, even if there are more than one with the same value.

Mind the input validation.

Example
{ 6, 2, 1, 8, 10 } => 16
{ 1, 1, 11, 2, 3 } => 6

Input validation
If an empty value ( null, None, Nothing etc. ) is given instead of an array,
or the given array is an empty list or a list with only 1 element, return 0. 
"""

def get_sum_from_list(list :list):

    if list == None:
        return 0
    
    if len(list) < 3:
        return 0
    
    if len(list) >= 3:
        list.sort()
        list.pop(0)
        list.pop(-1)
        total = 0
        for number in list:
            total += number

        return total
    """ 
     def sum_array(arr):
    return sum(sorted(arr)[1:-1]) if arr else 0

    a sum method exists so don't need a for loop
    can using slicing to remove fist and last elements
    and can use the if statement within the return statement
     
    also min max methods
    def sum_array(arr):
    if arr == None or len(arr) < 3:
        return 0
    return sum(arr) - max(arr) - min(arr)
       """