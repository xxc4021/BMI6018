# -*- coding: utf-8 -*-
"""
#%% the humble print statement
'''
1.a
Using the print() function only, get the wrong_add_function to print out where
it is making a mistake, given the expected output for ex, "we are making an error 
in the loop", which you would put near the loop. 
Structure the print() statement to show what the expected output ought to be
via f-strings: ie "The correct answer is supposed to be: [...]".
1.b
Then, changing as little as possible, modify the function, using the same 
general structure to output the correct answer. Call this new function 
correct_add_function() 
'''
def wrong_add_function(arg1,arg2):
   '''
   The function takes in two lists of integers, then it adds
   all of arg2 to each item of arg1.
   
   Example:
      > wrong_add_function([1,2,3],[1,1,1])
      > [6,9,12]

   whereas the expected correct answer is, [2,3,4]

   Parameters
   ----------
   arg1 : list
      list of integers.
   arg2 : list
      list of integers.

   Returns
   -------
   arg1 : list
      Elements of arg1, with each element having had the contents of 
      arg2 added to it.

   '''
   arg1_index=0
   while arg1_index < len(arg1):
      arg_2_sum = 0
      for arg2_elements in arg2:
         arg_2_sum = sum([arg1[arg1_index]+i for i in arg2])
      arg1[arg1_index]=arg_2_sum  
      arg1_index+=1
   return arg1

arg1 = [1,2,3]
arg2 = [1,1,1]

wrong_add_function(arg1, arg2)

#%% try, except
'''
2.a
Update the numeric section of the function with your changes from 1 for both 
2.b and 2.c

2.b
Without modifying the string section code itself or the input directly, 
write a try, except block that catches the issue with the input below and 
returns an error message to the user, in case users give invalid inputs,
(for example an input of ["5","2", 5])
: "Your input argument [1 or 2] at element [n]
is not of the expected type. Please change this and rerun. Name this function 
exception_add_function()

2.c
Without modifying the string section code itself or the input directly, 
write a try, except block that catches the issue with the input below and 
gets it to process via the string section. IE, do not, outside the function,
change the values of arg_str_1 or arg_str_2. Name this function 
correction_add_function(), i.e you will not be updating the wrong_add_function,
you will simply handle the error of wrong inputs in a seperate function, you want
the wrong_add_function to output its current result you are only bolstering the 
function for edge cases .
'''
def wrong_add_function(arg1,arg2):
   '''
   The function takes in two lists of integers, then it adds
   all of arg2 to each item of arg1.
   
   Example:
      > wrong_add_function([1,2,3],[1,1,1])
      > [4,5,6]
   
   If the lists are lists of strings, concatenate them
   Example:
      > wrong_add_function(['1','2','3'],['1','1','1'])
      > ['1111','2111','3111']
   Parameters
   ----------
   arg1 : list
      list of integers.
   arg2 : list
      list of integers.

   Returns
   -------
   arg1 : list
      Elements of arg1, with each element having had the contents of 
      arg2 added to it.

   '''
   #numeric section
   if sum([type(i)==int for i in arg1])==len(arg1) and \
      sum([type(i)==int for i in arg2])==len(arg2):
         arg1_index=0
         while arg1_index < len(arg1):
            arg_2_sum = 0
            for arg2_elements in arg2:
               arg_2_sum = sum([arg1[arg1_index]+i for i in arg2])
            arg1[arg1_index]=arg_2_sum  
            arg1_index+=1
         return arg1
   #string section
   elif sum([type(i)==str for i in arg1])==len(arg1) and \
      sum([type(i)==str for i in arg2])==len(arg2):
         arg1_index=0
         while arg1_index < len(arg1):
            arg_2_sum = ''
            for arg2_elements in arg2:
               arg_2_sum += arg2_elements
            arg1[arg1_index]=arg1[arg1_index]+str(arg_2_sum)
            arg1_index+=1
         return arg1
arg_str_1=['1','2','3']
arg_str_2=['1','1', 1]

wrong_add_function(arg_str_1,arg_str_2)

"""


# 1.a
print("[1.a]")


def wrong_add_function(arg1, arg2):
    arg1_index = 0
    while arg1_index < len(arg1):
        arg_2_sum = 0
        for arg2_elements in arg2:
            arg_2_sum = sum([arg1[arg1_index] + i for i in arg2])
        correct_answer = arg1[arg1_index] + arg2[arg1_index]
        if correct_answer != arg_2_sum:
            print("we are making an error in the loop")
            print(f"The answer is supposed to be: {correct_answer}")
        arg1[arg1_index] = arg_2_sum
        arg1_index += 1
    return arg1


arg1 = [1, 2, 3]
arg2 = [1, 1, 1]
arg3 = [arg1[i] + arg2[i] for i in range(len(arg1))]
wrong_add_function(arg1, arg2)
print(f"The correct answer is supposed to be: {arg3}")


# 1.b
print("[1.b]")


def correct_add_function(arg1, arg2):
    arg1_index = 0
    while arg1_index < len(arg1):
        arg_2_sum = arg1[arg1_index] + arg2[arg1_index]
        correct_answer = arg1[arg1_index] + arg2[arg1_index]
        if correct_answer != arg_2_sum:
            print("we are making an error in the loop")
            print(f"The answer is supposed to be: {correct_answer}")
        arg1[arg1_index] = arg_2_sum
        arg1_index += 1
    return arg1


arg1 = [1, 2, 3]
arg2 = [1, 1, 1]
print("The correct answer is supposed to be:", correct_add_function(arg1, arg2))

# 2.a
print("[2.a]")
def wrong_add_function(arg1, arg2):
    """
    The function takes in two lists of integers, then it adds
    all of arg2 to each item of arg1.

    Example:
       > wrong_add_function([1,2,3],[1,1,1])
       > [4,5,6]

    If the lists are lists of strings, concatenate them
    Example:
       > wrong_add_function(['1','2','3'],['1','1','1'])
       > ['1111','2111','3111']
    Parameters
    ----------
    arg1 : list
       list of integers.
    arg2 : list
       list of integers.

    Returns
    -------
    arg1 : list
       Elements of arg1, with each element having had the contents of
       arg2 added to it.

    """
    # numeric section
    if sum([type(i) == int for i in arg1]) == len(arg1) and sum(
        [type(i) == int for i in arg2]
    ) == len(arg2):
        arg1_index = 0
        while arg1_index < len(arg1):
            arg_2_sum = arg1[arg1_index] + arg2[arg1_index]
            correct_answer = arg1[arg1_index] + arg2[arg1_index]
            if correct_answer != arg_2_sum:
                print("we are making an error in the loop")
                print(f"The answer is supposed to be: {correct_answer}")
            arg1[arg1_index] = arg_2_sum
            arg1_index += 1
        return arg1
    # string section
    elif sum([type(i) == str for i in arg1]) == len(arg1) and sum(
        [type(i) == str for i in arg2]
    ) == len(arg2):
        arg1_index = 0
        while arg1_index < len(arg1):
            arg_2_sum = ""
            for arg2_elements in arg2:
                arg_2_sum += arg2_elements
            arg1[arg1_index] = arg1[arg1_index] + str(arg_2_sum)
            arg1_index += 1
        return arg1


arg_str_1 = ["1", "2", "3"]
arg_str_2 = ["1", "1", 1]

print(wrong_add_function(arg_str_1, arg_str_2))

# 2.b
print("[2.b]")


def except_add_function(arg1, arg2):
    """
    The function takes in two lists of integers, then it adds
    all of arg2 to each item of arg1.

    Example:
       > wrong_add_function([1,2,3],[1,1,1])
       > [4,5,6]

    If the lists are lists of strings, concatenate them
    Example:
       > wrong_add_function(['1','2','3'],['1','1','1'])
       > ['1111','2111','3111']
    Parameters
    ----------
    arg1 : list
       list of integers.
    arg2 : list
       list of integers.

    Returns
    -------
    arg1 : list
       Elements of arg1, with each element having had the contents of
       arg2 added to it.

    """
    # numeric section
    try:
        if sum([type(i) == int for i in arg1]) == len(arg1) and sum(
            [type(i) == int for i in arg2]
        ) == len(arg2):
            arg1_index = 0
            while arg1_index < len(arg1):
                arg_2_sum = arg1[arg1_index] + arg2[arg1_index]
                correct_answer = arg1[arg1_index] + arg2[arg1_index]
                if correct_answer != arg_2_sum:
                    print("we are making an error in the loop")
                    print(f"The answer is supposed to be: {correct_answer}")
                arg1[arg1_index] = arg_2_sum
                arg1_index += 1
            return arg1
        # string section
        elif sum([type(i) == str for i in arg1]) == len(arg1) and sum(
            [type(i) == str for i in arg2]
        ) == len(arg2):
            arg1_index = 0
            while arg1_index < len(arg1):
                arg_2_sum = ""
                for arg2_elements in arg2:
                    arg_2_sum += arg2_elements
                arg1[arg1_index] = arg1[arg1_index] + str(arg_2_sum)
                arg1_index += 1
            return arg1
        else:
            raise TypeError
    except TypeError:
        # default is all str
        for arg1_index in range(len(arg1)):
            if not isinstance(arg1[arg1_index], str):
                print(f"arg1 list's item {arg1_index} is not a str")

        for arg2_index in range(len(arg2)):
            if not isinstance(arg2[arg2_index], str):
                print(f"arg1 list's item {arg2_index} is not a str")
        return


arg_str_1 = ["1", "2", "3"]
arg_str_2 = ["1", "1", 1]

print(except_add_function(arg_str_1, arg_str_2))

# 2.c
print("[2.c]")


def correct_add_function(arg1, arg2):
    return [str(a1) + str(a2) for a1, a2 in zip(arg1, arg2)]

def wrong_add_function(arg1, arg2):
    """
    The function takes in two lists of integers, then it adds
    all of arg2 to each item of arg1.

    Example:
       > wrong_add_function([1,2,3],[1,1,1])
       > [4,5,6]

    If the lists are lists of strings, concatenate them
    Example:
       > wrong_add_function(['1','2','3'],['1','1','1'])
       > ['1111','2111','3111']
    Parameters
    ----------
    arg1 : list
       list of integers.
    arg2 : list
       list of integers.

    Returns
    -------
    arg1 : list
       Elements of arg1, with each element having had the contents of
       arg2 added to it.

    """
    try:
      # numeric section
      if sum([type(i) == int for i in arg1]) == len(arg1) and sum(
         [type(i) == int for i in arg2]
      ) == len(arg2):
         arg1_index = 0
         while arg1_index < len(arg1):
               arg_2_sum = arg1[arg1_index] + arg2[arg1_index]
               correct_answer = arg1[arg1_index] + arg2[arg1_index]
               if correct_answer != arg_2_sum:
                  print("we are making an error in the loop")
                  print(f"The answer is supposed to be: {correct_answer}")
               arg1[arg1_index] = arg_2_sum
               arg1_index += 1
         return arg1
      # string section
      elif sum([type(i) == str for i in arg1]) == len(arg1) and sum(
         [type(i) == str for i in arg2]
      ) == len(arg2):
         arg1_index = 0
         while arg1_index < len(arg1):
               arg_2_sum = ""
               for arg2_elements in arg2:
                  arg_2_sum += arg2_elements
               arg1[arg1_index] = arg1[arg1_index] + str(arg_2_sum)
               arg1_index += 1
         return arg1
      else:
          raise TypeError
    except TypeError:
        return correct_add_function(arg1,arg2)


arg_str_1 = ["1", "2", "3"]
arg_str_2 = ["1", "1", 1]

print(wrong_add_function(arg_str_1, arg_str_2))
