dic = {"Atta": "Human Being", "Spoon": "Object"}
print(dic["Atta"])

dic = {11: "Ayesha", 12: "Amna", 13: "Rubina", 14: "Atta"}
print(dic[11])

info = {"name": "Atta", "age": 24, "eligible": True}
print(info)

print(info["name"])  # this will through error if value is not present
print(info.get("name"))  # this will not through error if value is not present

# Accessing all keys

print(info.keys())
print(info.values())

for key in info:
    print(key)


print(info.items())

for key, value in info.items():
    print(f"The value corresponding to {key} is {value}")
