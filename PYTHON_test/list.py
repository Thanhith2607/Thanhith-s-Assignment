data = [10, 20, 30, 40, 50, 20, 30, 60, 70, 80, 90]

data.append([100,110])
print(data)

data.extend([120, 130])
print(data)

data.insert(2, 25)
print(data)

data.remove(20)
print(data)

last_element = data.pop()
print(data)


data.reverse()
print(data)



