# 1
""""
Write a Python program that takes a list of numbers as input, removes duplicates using a suitable list method, and returns a dictionary containing the original list, the unique values, and their count. Use a function with parameters and a return statement to perform this task.

"""
def  list_processing (original_list):
    temp_list = original_list.copy()
    temp_list.sort()
    for i in temp_list:
        duplicate_count = temp_list.count(i)
        if duplicate_count>1:
            i_index = temp_list.index(i)
            while i_index+1<i_index+duplicate_count:
                del temp_list[i_index]
                duplicate_count=duplicate_count-1
    return {
        "original_list": original_list,
        "unique_values":temp_list,
        "unique_values_count":len(temp_list)
    }
number_list=[]
for i in range(1,6):
    number_list.append(int(input("Take a number: ")))
final_result = list_processing(number_list)
print(final_result)
# 2
"""
Create a function that accepts two sets as parameters and returns their union, intersection, and difference. Use keyword arguments with default parameter values so the function can work even if one of the sets is not provided by the user. Display the results clearly.
"""
def process_set(first_set={2,4,2,7,9},second_set={7,1,9,3,7,2}):
    union_set = first_set.union(second_set)
    intersection_set = first_set.intersection(second_set)
    difference_set = first_set.difference(second_set)
    return {
        "Union": union_set,
        "Intersection": intersection_set,
        "Difference": difference_set
    }
set_1 = {2,4,2,7,9}
set_2 = {7,1,9,3,7,2}
result = process_set(set_1,set_2 )
print(result)
