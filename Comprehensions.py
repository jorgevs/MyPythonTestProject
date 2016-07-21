
new_list = [x for x in range(5)]

# This will create a list from 0-5. It is the equivalent of the following for loop:
#new_list = []
#for x in range(5):
#    new_list.append(x)

# A dict comprehension is similar. It looks like this:
new_dict = {key: str(key) for key in range(5)}

# A set comprehension will create a Python set, which means you will end up with an unordered collection with no duplicates.
new_set = {x for x in 'mississippi'}


print new_list
print new_dict
print new_set

