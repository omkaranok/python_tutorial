##Dictionaries
band = {
    "vocals":"Plant",    #is similar to javascript object
    "guitar":"page"      ##in python dict is used in placed of object 
}

band2 = dict(vocals = "Plant",guitar="Page")
print(band)
print(band2)
print(type(band))
print(len(band))

##Access item of dictionary
print(band["vocals"])
print(band.get("guitar"))


##list all key
print(band.keys())

##list all values
print(band.values())

##list of key/values pairs
print(band.items())

print("guitar" in band)

band["vocals"] = "Robert Plant"
print(band)
band.update({"bass":"JPJ"})
print(band)

print(band.pop("bass"))  ##pop only rerurn s value of the key
print(band)

band["drums"] = "Bonham"
print(band)
print(band.popitem())  ##popitem returns the last item of the dictionary as a tuple
print(band)


##Delete and clear items
band["drums"] = "Bonham"
print(band)
del band["drums"]  ##delete the key and value
print(band)

band2.clear()
print(band2)

del band2


band2 = band     ##copy as a reference
print("Bad copy!")

# band2["drums"] = "Dave"
print(band)

# del band["drums"]

band2 = band.copy()
band2["drums"] = "Dave"
print("Good copy!")
print(band)
print(band2)

##or use the dict() constructor
band3 = dict(band)
print("Good copy")
print(band3)


####Nested dictionaries#####
memeber1 = {
    "name":"Plant",
    "instrument":"vocals",
}

memeber2 = {
    "name":"Page",
    "instrument":"guitar",
}

band= {
    "member1": memeber1,
    "member2": memeber2
}

print(band)

print(band["member1"]["name"])
print(band["member2"]["instrument"])   #we can even acces the nested dictionary items

##########################Sets###########################

nums = { 1,2,3,4,5,}
nums2 = set((1,2,3,4,5))

print(nums)
print(nums2)
print(type(nums))
print(len(nums))


###No dublicates are allowed in sets
nums = {1,2,2,3,45}
print(nums)


##True is a dupe of 1,False is a dupe of 0

nums = {1,2,3,4,5,True,False,0}
print(nums)  #True is a duplicate of 1, False is a duplicate of 0

print(2 in nums)

##but you cannot refer to an element in the set with an index position or  a key
## Add a new element to the set

nums.add(6)    ###addd methos is used to add the element in the sets
print(nums)

morenums = {5,6,7}
nums.update(morenums)
nums.update(band)
print(nums)


###in sets, you can update the set with lists,tuples and other sets

##Merge two sets to create a new sets 
one = {1,2,3}
two = {4,5,6}

mynewset = one.union(two)
print(mynewset)


##Intersection of two sets
myset1 = {1,2,3,4,5}
myset2 = {3,4,5,6,7}

myset1.intersection_update(myset2)  #update the first set with the intersection of both sets
print(myset1)

###keep everthing except the dublicates####
one = {1,2,3,4,5}
two = {3,4,5,6,7}

one.symmetric_difference_update(two)  #update the first set with the symmetric difference of both sets
print(one)


three = {1,2,3,4,5}
four = {3,4,5,6,7}

three.union(four)  #union method returns a new set with the union of both sets so we have to upadte it in new varible
print(three)