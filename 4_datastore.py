# Below is a dictionary that contains information about real estate space for
# a doctor's office. Using the dictionary, create a csv file that has details
# for each space represented as rows. Name your file 'retail_space.csv.


"""
Your final output should look like:

room-number,use,sq-ft,price
100,reception,50,75
101,waiting,250,75
102,examination,125,150
103,examination,125,150
104,office,150,100

"""

# datastore has 1 key: medical
# the value of medical is a list of 5 dictionaries
# the keys are the same for all of the dictionaries

datastore = {
    "medical": [
        {"room-number": 100, "use": "reception", "sq-ft": 50, "price": 75},
        {"room-number": 101, "use": "waiting", "sq-ft": 250, "price": 75},
        {"room-number": 102, "use": "examination", "sq-ft": 125, "price": 150},
        {"room-number": 103, "use": "examination", "sq-ft": 125, "price": 150},
        {"room-number": 104, "use": "office", "sq-ft": 150, "price": 100},
    ]
}

outfile = open("retail_space.csv", "w")

outfile.write("room-number,use,sq-ft,price\n")

mylist = datastore["medical"]
print(type(mylist))

# for l in datastore["medical"]:
#  print(type(l)) #l refers to each element in that list, l is a dictionary

for l in mylist:
    outfile.write(
        str(l["room-number"])
        + ","
        + l["use"]
        + ","
        + str(l["sq-ft"])
        + ","
        + str(l["price"])
        + "\n"
    )


outfile.close()
