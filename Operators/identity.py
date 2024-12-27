x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print (x is z)
# returns true

print(x is y)
# returns false 
# values are same but objects are different

print (x == y)
#return true
# It compare the values


print(x is not z) #returns false
print(x is not y) #returns True
print (x != y) # returns false