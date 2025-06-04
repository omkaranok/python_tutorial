def square(num): return num * num

print(square(5))

squared = lambda num: num* num
print(squared(5))

addTw0 = lambda num: num + 2
print(addTw0(5))

sum_two = lambda num1, num2: num1 + num2
print(sum_two(5, 3))


######################################################
def funcBuilder(x):
    return lambda num: x + num    ### here we are using loambda as a function which returns a functions that takes a number later which will get replaced by num

addTen = funcBuilder(10)
addTwenty = funcBuilder(20)
print(addTen(5))  # Output: 15
print(addTwenty(5))  # Output: 25



###############Higher Order Functions###################### that accept one function as a params or return another function as a result

numbers = [1,2,3,4,5]

squared_numbers = map(lambda x:x*x,numbers)  #map function applies the lambda function to each element in the numbers list whicch accept two parameter as input

print(list(squared_numbers))  # Output: <map object at 0x...>
####Higher order function receives function as argument or retyrn function as argument#################################

###############Filter functions##############################
odd_nums = filter(lambda num:num%2 !=0,numbers)   ### here filter which filter elemkent according to true and false will return only of true
print(list(odd_nums))


#############################Reduce function######################################
from functools import reduce
lambda acc,curr: curr+ acc

numbers = [1,2,3,4,5]          ####we can use reduce function to0 apply a function cummlatively to the items of iterable, from left to right, so as to reduce the iterable to a single value.
sum_of_numbers = reduce(lambda acc, curr: curr + acc, numbers,10)  #reduce function applies the lambda function cumulatively to the items of the iterable, from left to right, so as to reduce the iterable to a single value.


print(sum_of_numbers)  # Output: 15
print(sum(numbers,10))  # Output: 25, here we are using the built in sum function to get the sum of the numbers list with an initial value of 10

names = ["Neil","John","Dave","Jimmy jimmyy aa ajj"]
char_count = reduce(lambda acc,curr:acc+len(curr), names, 0)  # here we are using reduce function to get the total number of characters in the names list, starting with an initial value of 0
print(char_count)  # Output: 26, here we are using the reduce function to get the total number of characters in the names list, starting with an initial value of 0