t = (10, 20, 30, 40, 50, 20, 60)

count_20 = t.count(20)
print(count_20)

index_40 = t.index(40)
print(index_40)

temp = list(t)
temp.append(70)
t = tuple(temp)

print(t)

slice_t = t[2:6]
print(slice_t)

t = t + (80, 90)
print(t)

t2 = t * 2
print(t2)

print(50 in t)

a, b, c, d, e, f, g, h, i = t
print(a, b)