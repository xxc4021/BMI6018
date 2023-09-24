"""
Write a python program that, given an input list, will filter the input above a user defined threshold. This is to be done with a standard function.
That is, given a list [1,2,3,4,5,6,7,8,9], and an argument (6), it should return [1,2,3,4,5,6]
"""
def filter(input_list,argument):
    return [a for a in input_list if a <= argument]
input_list = [1,2,3,4,5,6,7,8,9]
argument = 6
print(filter(input_list,argument))
