# 1. Define the id of next variables:
int_a = 55 # integer
str_b = 'cursor' # string
set_c = {1, 2, 3} # set
lst_d = [1, 2, 3] # list
dict_e = {'a': 1, 'b': 2, 'c': 3} # dictionary
print("1.defiition of variables:")
print("[int_a id is:",id(int_a),
      "] [str_b id is:",id(str_b),
      "] [set_c id is:",id(set_c),
      "] [lst_d id is:",id(lst_d),
      "] [dict_e id is:",id(dict_e),
      "]")
print()


#2. Append 4 and 5 to the lst_d and define the id one more time.
apdt = [4, 5]
lst_d.append(apdt)
print("2. Append 4 and 5 to the lst_d and define the id one more time result is:")
print("a) Appended 4 and 5 to lst_d result :",lst_d)
print()
print("b) Redefinition of id is:")
print("[int_a id is:",id(int_a),
      "] [str_b id is:",id(str_b),
      "] [set_c id is:",id(set_c),
      "] [lst_d id is:",id(lst_d),
      "] [dict_e id is:",id(dict_e),
      "]")
print()

# 3. Define the type of each object from step 1.
print("3. Define the type of each object from step 1 result is: ")
print("[Variable int_a is : ", type(int_a),
      "] [Variable str_b is : ", type(str_b),
      "] [Variable set_c is : ", type(set_c),
      "] [Variable lst_d is : ", type(lst_d),
      "] [Variable dict_e is : ", type(dict_e),
      "]")
print()
#4*. Check the type of the objects by using isinstance.

print("4*.Types of the objects by using isinstance is:")
def classtypeisinstance(classtype):
    if isinstance(classtype,int)==True :
        return(" is int")
    else:
        if isinstance(classtype,str)==True :
            return(" is str")
        else:
            if isinstance(classtype, set) == True:
                return(" is set")
            else:
                if isinstance(classtype, list) == True:
                    return(" is list")
                else:
                    if isinstance(classtype, dict) == True:
                        return(" is dict")
                    else:
                        return(" class is not confirmed")

print ("[int_a :",classtypeisinstance(int_a),
       "] [str_b :",classtypeisinstance(str_b),
       "] [set_c :",classtypeisinstance(set_c),
       "] [lst_d :",classtypeisinstance(lst_d),
       "] [dict_e :",classtypeisinstance(dict_e),
       "]")
#String formatting:
#Replace the placeholders with a value:
#"Anna has ___ apples and ___ peaches
#5. With .format and curly braces {}
#6. By passing index numbers into the curly braces.
#7. By using keyword arguments into the curly braces.
#8*. With indicators of field size (5 chars for the first and 3 for the second)
#9. With f-strings and variables
#10. With % operator
#11*. With variable substitutions by name (hint: by using dict)

print("Initial text is: Anna has ___ apples and ___ peaches ")
print()

print("5.Replaced the placeholders with a value with .format and curly braces {} :")
print( "Anna has {} apples and".format(3), "{}peaches.".format(5))
print()
print("6. By passing index numbers into the curly braces:")
print("Anna has {1} apples and {0} peaches".format(5, 3))
print()
print("7. By using keyword arguments into the curly braces:")
print( "Anna has {qty1} apples and {qty2} peaches.".format(qty1=3, qty2=5))
print()
print("#8*. With indicators of field size (5 chars for the first and 3 for the second")
print( "Anna has {0:>5s} apples and {1:>5s} peaches.".format("three", "five"))
print()
print("#9. With f-strings and variables")
apples=3
peaches=5
print( f"Anna has {apples} apples and {peaches} peaches.")
print()
print("#10. With % operator")
apples=3
peaches=5
print( f"Anna has %s apples and %s peaches." % (apples, peaches))
print()
print("11. With variable substitutions by name (hint: by using dict)")
apples=3
peaches=5
fruits_dict = {"a": apples, "p": peaches}
print( "Anna has %(a)s apples and %(p)s peaches." %fruits_dict)
print()

#         (1)
#         lst = []
#         for num in range(10):
#             if num % 2 == 1:
#                 lst.append(num ** 2)
#             else:
#                lst.append(num ** 4)
#        print(lst)
#       (2)
#        list_comprehension = [num // 2 if num % 2 == 0 else num * 10 for num in range(10)]

print ("12. Convert (1) to list comprehension")
print("12 Version 1:")
lst = []
for num in range(10):
    if num % 2 == 1:
        lst.append(num ** 2)
    else:
        lst.append(num ** 4)
print(lst)
print ("12 List comprihension version:")

lst_1 = [num ** 2  if num %2 == 1 else num ** 4 for num in range (10)]

print (lst_1)
print ("13. Convert (2) to regular for with if-else:")
print("13 list_comprehension:")
list_comprehension = [num // 2 if num % 2 == 0 else num * 10 for num in range(10)]
print (list_comprehension)
print ("13 Converted version:")
lst = []
for num in range (10):
    if num % 2 == 0:
        lst.append(num // 2)
    else:
        lst.append(num*10)
print (lst)
# (3)
# d = {}
# for num in range(1, 11):
#     if num % 2 == 1:
#         d[num] = num ** 2
# print(d)
#
# (4)
# d = {}
# for num in range(1, 11):
#     if num % 2 == 1:
#         d[num] = num ** 2
#     else:
#         d[num] = num // 0.5
# print(d)
#
# (5)
# dict_comprehension = {x: x**3 for x in range(10) if x**3 % 4 == 0}
#
# (6)
# dict_comprehension = {x: x**3 if x**3 % 4 == 0 else x for x in range(10)}
#

print ("# 14. Convert (3) to dict comprehension:")
print ("14 initial method (3):")
d = {}
for num in range(1, 11):
     if num % 2 == 1:
         d[num] = num ** 2
print(d)
print ("14 converted to list of comprihension method (3):")
dict_1 = {num: num **2 for num in range (1, 11) if num % 2 == 1 }
print (dict_1)

print ("15*. Convert (4) to dict comprehension.")
print ("15 initial method (4):")
d = {}
for num in range(1, 11):
     if num % 2 == 1:
         d[num] = num ** 2
     else:
         d[num] = num // 0.5
print (d)
print ("15  method list comprihension:")

dict_2 = { num: num ** 2 if num % 2 == 1 else num //0.5 for num in range (1, 11) }
print (dict_2)

print (" 16. Convert (5) to regular for with if.")
print ("16 initial method (5):")
dict_comprehension = {x: x**3 for x in range(10) if x**3 % 4 == 0}
print (dict_comprehension)

print ("16  converted to regular")
dict_reg = {}
for x in range (10):
    if x ** 3 % 4 == 0:
        dict_reg[x] = x ** 3
print (dict_reg)

print (" 17*. Convert (6) to regular for with if-else.")
print ("17 initial method (6):")
dict_comprehension = {x: x**3 if x**3 % 4 == 0 else x for x in range(10)}
print (dict_comprehension)
print ("17  converted to regular")
dict_reg2 = {}
for x in range (10):
    if x ** 3% 4 == 0:
        dict_reg2[x] = x ** 3
    else:
        dict_reg2[x] = x
print (dict_reg2)
print ("Lambda:")
print ("18*. Convert (6) to regular for with if-else.")
print (" Convert (7) to lambda function")
print ("Initial regular function method")
x = 3
y = 5
def foo(x, y):
    if x < y:
        return x
    else:
        return y
print (foo(x,y))
print ("Converted (7) to Lambda method")
foo_l = lambda x,y: x if x<y else y
print (foo_l(x, y))

print ("19*. Convert (8) to regular function")
print ("Initial lambda method:")
x = 3
y = 5
z = 20
foo = lambda x, y, z: z if y < x and x > z else y
print (foo(x, y, z))
print ("Converted to regular function method")
def foo_r (x, y, z):
    if y < z  and  x > z:
        return z
    else:
        return y
print (foo_r(x, y, z))
from functools import reduce

print (" lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]")
print ("20. Sort lst_to_sort from min to max")
lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]
print ("lst_to_sort:", lst_to_sort)
lst_sorted = sorted (lst_to_sort)
print ("List sorted min-max:", lst_sorted)

print ("21. Sort lst_to_sort from max to min")
lst_sorted_r = sorted (lst_to_sort, reverse=True)
print ("Sorted max - min list:",lst_sorted_r)
print ("22. Use map and lambda to update the lst_to_sort by multiply each element by 2")
mult_2 = list (map (lambda elem: elem * 2, lst_to_sort))
print ("List of multiplied elements by 2:", mult_2)
print ("23*. Raise each list number to the corresponding number on another list:")
print ("list_A = [2, 3, 4]")
print ("list_B = [5, 6, 7]")
list_A = [2, 3, 4]
list_B = [5, 6, 7]
mult_ab = list (map (lambda a,b: a * b, list_A, list_B))
print ("List multiplied list by list:", mult_ab)
print("24. Use filter and lambda to filter the number of a lst_to_sort with elem % 2 == 1.")
print (" lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]")
lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]
print (lst_to_sort)

print ("filtered list:")
filtred_l = list(filter (lambda elem: elem % 2 == 1, lst_to_sort))
print (filtred_l)

print ("# 25. Considering the range of values: b = range(-10, 10), use the function filter to return only negative numbers.")
b = list (range(-10, 10))
print ("List range b")
print (b)
filtred_ln = list (filter (lambda elemn: elemn < 0, b ))
print ("Sorted List range b <0 :")
print (filtred_ln)

print ("#26. Using the filter function, find the values that are common to the two lists:")
list_1 = [1,2,3,5,7,9]
list_2 = [2,3,5,6,7,8]
print ("list_1:", list_1)
print ("list_2:", list_2)
c_list = list(filter(lambda elem_c: elem_c in list_2, list_1))
print (c_list)

