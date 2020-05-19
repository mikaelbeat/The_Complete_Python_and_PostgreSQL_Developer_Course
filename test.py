

data = {"name": "Demo", "marks": [10, 20, 30]}

#print(len(["Demo"]))
print(len(data["marks"]))
print(sum(data["marks"]))

marks_sum = sum(data["marks"])
marks_added = len(data["marks"])

print(marks_sum / marks_added)



def print_data(data):
    print(data["name"])

print_data(data)