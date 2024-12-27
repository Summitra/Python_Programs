"""age = 21
txt = "My name is Sumitra, I am " +age
print(txt)""" # this will throw error becase
# we cannot concatenate string with number

"""age = 21
txt = f"My name is Sumitra, I am {age}"
print(txt)"""

price = 60
txt = f"The price is {price} dollars"
print(txt)

price = 70
txt = f"The price is {price :.3f} dollars"
print(txt)

# another placeholder
txt = f"The price is {20 * 60} dollars"
print(txt)