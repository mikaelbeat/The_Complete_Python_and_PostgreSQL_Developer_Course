

numbers = [1, 2, 3]
doubled = [x * 2 for x in numbers]


friends = ["Rolf", "Sam"]
friends_s = [friend for friend in friends if friend.startswith("S")]

for friend in friends:
    if friend.startswith("S"):
        print(friend)