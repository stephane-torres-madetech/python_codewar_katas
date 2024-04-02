""" Take an array and remove every second element from the array. Always keep the first element and start removing with the next element.

Example:
["Keep", "Remove", "Keep", "Remove", "Keep", ...] --> ["Keep", "Keep", "Keep", ...]

None of the arrays will be empty, so you don't have to worry about that! """



def remove_every_other(array: list):
   """ list[start point for slice : end point(not inclusive for slice : step/increment)] 
       if start and end are left blank e.g array[::2] start is assumed at 0 and end is assumed length of list"""
   return array[::2] 
