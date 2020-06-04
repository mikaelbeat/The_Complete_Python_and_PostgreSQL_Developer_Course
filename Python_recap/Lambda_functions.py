
# lambda x, y: x + y

add = lambda x, y: x + y

print(add(5, 7))


data = [1, 2, 3, 4]

# mao function runs lambda function to each value in data
doubled = list(map(lambda x: x * 2, data))
print(doubled)