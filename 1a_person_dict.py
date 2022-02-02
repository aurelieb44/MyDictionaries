person = {}
person["fname"] = "Joe"
person["lname"] = "Fonebone"
person["age"] = 51
person["spouse"] = "Edna"
person["children"] = ["Ralph", "Betty", "Joey"]  # list
person["pets"] = {"dog": "Fido", "cat": "Sox"}  # dictionary


# the value for cat may be an other dictionnary, you could go as deep as you want.
# print(person)

# print(type(person["children"]))

print(
    person["children"][2]
)  # 2 is the index location of where Betty is #children is a key

print()

print(person["pets"]["cat"])  # dictionary within a dictionary, we give it the key
# print the value for the key cat.

print()

for i in person[
    "children"
]:  # children is a list, #i is an iterator through each element of the list
    print(i)

print()

for i, j in person["pets"].items():  # j is the value #i is the key
    print(i)
    print(j)
