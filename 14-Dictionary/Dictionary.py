friends = {'tom': '111-222-333', 'jerry': '666-444-555'}
print(friends)  # {'tom': '111-222-333', 'jerry': '666-444-555'}

# retrieving
print(friends['tom'])  # 111-222-333

# add new element
friends['bob'] = '888-999-444'
print(friends)  # {'tom': '111-222-333', 'jerry': '666-444-555', 'bob': '888-999-444'}

# modify the element
friends['bob'] = '111-333-333'
print(friends)  # {'tom': '111-222-333', 'jerry': '666-444-555', 'bob': '111-333-333'}

# deleting item
del friends['bob']
print(friends)  # {'tom': '111-222-333', 'jerry': '666-444-555'}

# Looping items
for x in friends:
    print(x, ":", friends[x])  # tom : 111-222-333      jerry : 666-444-555

# length
print(len(friends))  # 2

# equality
d1 = {"mike": 41, "bob": 35}
d2 = {"bob": 20, "mike": 41}
print(d1 == d2)    # False   order is not important
print(d1 != d2)    # True

# dictionary methods
friends = {'tom': '111-222-333', 'jerry': '666-444-555', 'bob': '888-999-444'}
print(friends.popitem())   # ('bob', '888-999-444')      returns randomly select item and remove
print(friends)   # {'tom': '111-222-333', 'jerry': '666-444-555'}

friends.clear()     # delete everything
print(friends)      # {}

friends = {'tom': '111-222-333', 'jerry': '666-444-555', 'bob': '888-999-444'}

print(friends.keys())  # dict_keys(['tom', 'jerry', 'bob'])    returns keys as tuples

print(friends.values())  # dict_values(['111-222-333', '666-444-555', '888-999-444'])   returns values as tuples

print(friends.get("tom"))   # 111-222-333    if not found  returns None
print(friends.get("jim"))   # None

print(friends.pop("tom"))    # 111-222-333   remove the item if not found throw error
print(friends)     # {'jerry': '666-444-555', 'bob': '888-999-444'}
