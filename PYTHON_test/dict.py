student = {
    "name": "John",
    "age": 21,
    "marks": {"math": 80, "science": 90}
}

print(student.get("name"))

student["grade"] = "A"
print(student.get("grade"))

student.update({"age": 22})
print(student.get("age"))

removed_age = student.pop("age")
print(removed_age)

last_item = student.popitem()
print(last_item)

print(student.keys())


print(student.values())

print(student.items())