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
