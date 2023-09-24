"""
Write the a python program that, given an input list of any level of complexity/nestedness, will return the inner most list plus 1. This is to be done with recursion. Note: the input will contain only integers or lists. 
"""
def inner_most(item_list):
    empty1 = []
    empty2 = []
    for x in item_list:
        if isinstance(x, list):
            for a in x:
                empty1.append(a) 
        else:
            empty2.append(x)
    item_list = empty1
    if len(item_list) > 0:
        return inner_most(item_list)
    else:
        return [i + 1 for i in empty2]


item_list = [1, 2, [3, 4], [5, 6, 7, [8, 9]], [1, 2]]
print(inner_most(item_list))
