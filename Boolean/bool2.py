class myClass():
    def __len__(self):
        return 0
obj = myClass()
print(bool(obj))

# functions can return a boolean value
def myFunction():
    return True
print(myFunction())


def myFunction():
    return True
if myFunction():
    print("YES !!")
else:
    print("NO !")

# isinstance() method also return boolean value
x = 200.00
print(isinstance(x,int))