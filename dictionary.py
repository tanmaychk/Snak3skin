bag = dict()
bag["bottle "] = 4
bag["card"] = 67
bag["tiffin"] = 53
print(bag)


# simplified counting with "get"
count = dict()
names = ["csev", "name", "csev", "cane", "cane", "cane", "name"]
for name in names:
    count[name] = count.get(name, 0) + 1
print(count)
