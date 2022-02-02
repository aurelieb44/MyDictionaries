phonebook = {"Chris": "555−1111", "Katie": "555−2222", "Joanne": "555−3333"}
"""
print()
print("*****  start section 1 - print dictionary ********")
print()

print(phonebook)

print(len(phonebook))
print(type(phonebook))

mydictionary = dict(m=8, n=9)
print(mydictionary)

chris_phone = phonebook["Chris"]
print(chris_phone)

print()
print("*****  end section 1 ********")
print()


print()
print("*****  start section 2 - search dictionary ********")
print()

name = "Chris"

if name in phonebook:
    print(phonebook[name])
else:
    print(name, "is not in the phonebook")

print()
print("*****  end section 2 ********")
print()


print()
print("*****  start section 3 - edit/append dictionary ********")
print()

phonebook["Joe"] = "555-0123"  # creating Joe
phonebook["Chris"] = "555-4444"  # updating Chris' phone number.
print(phonebook)

print()
print("*****  end section 3 ********")
print()

print()
print("*****  start section 4 - delete/remove from dictionary ********")
print()

del phonebook["Chris"]
print(phonebook)

print()
print("*****  end section 4 ********")
print()


print()
print("*****  start section 5 - iterate through keys ********")
print()

for key in phonebook:
    print(key)  # print the key
    print(phonebook[key])  # print the corresponding value/phone number

print()
print("*****  end section 5 ********")
print()


print()
print("*****  start section 6 - iterate through values  ********")
print()


for value in phonebook.values():  # values is used as a method of the dictionary object
    print(value)

print()
print("*****  end section 6 ********")
print()

"""
print()
print("*****  start section 7 - iterate through both key and value pair********")
print()


for (
    phonebook_tuple
) in (
    phonebook.items()
):  # the items method allows us to have both the key and the value at the same time
    print(phonebook_tuple)
    print(type(phonebook_tuple))

print()

for (
    key,
    value,
) in (
    phonebook.items()
):  # we use two variables to have values for the key and the values separately
    print(key)
    print(value)


print()
print("*****  end section 7 ********")
print()
"""

print()
print("*****  start section 8 - using get and clear methods ********")
print()


phone = phonebook.get("Chris", "key not found")
print(phone)
phonebook.clear()
print(phonebook)


print()
print("*****  end section 8 ********")
print()


print()
print("*****  start section 9 - using pop and popitem ********")
print()


# remove = phonebook.pop('Chris', 'not found')
# print(remove)
# print(phonebook)

a = phonebook.popitem()
print(a)
print(phonebook)

print()
print("*****  end section 9 ********")
print()


import random

print()
print("*****  start section 10 - using random and converting to list ********")
print()


random_phone = list(phonebook)  # creates a list of keys/names of people
print(random_phone)
choice = random.choice(random_phone)
print(choice)
print(phonebook[choice])

print()
random_phone = phonebook[random.choice(list(phonebook))]
print(random_phone)

print()
print("*****  end section 10 ********")
print()
"""
