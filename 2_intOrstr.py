lst = [1, 'hello', 3, 'world']

result = all(map(lambda x: isinstance(x, (int)), lst))

print(result)