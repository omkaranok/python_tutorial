users = ["Dave","John","Sara"]
data = ["Dave",42,True]

emptylist = []

print("Dave" in users)

print("Dave" in emptylist)

print(users[0])
print(users[-2])

print(users.index("Dave"))
print(users.index("Sara"))

print(users[0:2])
print(users[1:])
print(users[-3:-1])

print(len(data))

users.append("Mary")
print(users)

###if we don't add the [""] it will add the single letter of every element in users lists
# users += "Jason"
users+= ['Jason']
print(users)

users.extend(["Tom","Jerry"])
print(users)

users.extend(data)
print(users)

print(users)

users.insert(0,'Bob')
print(users)

users[2:2] = ["Eddie", "Alex"]
print(users)

users[1:3] = ["robert","JPJ"]
print(users)

users.remove("Bob")
print(users)

print(users.pop())
print(users)

users.insert(0,"jaguar")
print(users)

print(users.pop())
print(users)

del users[0]
print(users)

# del data
# print(data)

data.clear()
print(data)

users[1:2] = ["dave"]
users.sort()
print(users)

users.sort(key=str.lower)
print(users)

nums = [1,2,3,45,6]
nums.reverse()
print(nums)

##for descending ordere lists printed is 
# nums.sort(reverse=True)
# print(nums)


##Global sorted functions
# print(nums)
# print(sorted(nums,reverse = True))
# print(nums)

# cars = sorted(nums,reverse=True)
# print(cars)


##make a copy of the lists first then sort it accordingly by three ways
numscopy = nums.copy()
mynums = list(numscopy)
mycopy = nums[:]

print("copy of nums")
print(numscopy)
print(mynums)
mycopy.sort()
print(mycopy)
print(nums)

print(type(nums))
mylists = list([1,"Neil",True])
print(mylists)


#tuples 

mytuple = tuple(("Dave",42,True))
anothertuple = ("John",30,True,8.5,8.5,8.5)
print(mytuple)
print(anothertuple)
print(type(mytuple))
print(type(anothertuple))

newlist = list(mytuple)
newlist.append("New Item")
newtuple = tuple(newlist)
print(mytuple)
print(newtuple)

###Unpacking the tuples
(one,*two,hey) = anothertuple
print(one)
print(two)
print(hey)

print(anothertuple.count(8.5))
print(users.pop())

anothertuple = mytuple
print(anothertuple)