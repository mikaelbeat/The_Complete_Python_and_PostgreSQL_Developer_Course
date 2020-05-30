
friends = {"Rolf": 34, "Anne": 27}

# Adding to dictionary works sameway than updating
friends["Adam"] = 30
friends["Rolf"] = 37

print(friends)


for friend, age in friends.items():
    print(f"{friend} - {age}")