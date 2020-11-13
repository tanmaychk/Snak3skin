# Changing items in a list
items = [23, 24, 56, 79]
print(items)
items[1] = 45
print(items)
######################
my_list = [1, 2, 3]
print(my_list)
my_list[2] = 4
print(my_list)

# adding items to a list (using while)
emp = list()
while True:
    name = input("whats your name? : ")
    emp.append(name)
    if name == "done":
        break
print(emp)

# counting stuff in a list
length = len(emp)  # counts number of items
counting = emp.count("lori")  # counts specific items
print(length, counting)

# sorting a list
emp.sort()
print(emp)

# splitting to form a list
st = " im ready to be splitted out "
pieces = st.split()
print(pieces)

# math ops in lists
# max .  min . sum . avg = sum/len
number = [1, 2, 3, 5, 6, 93, 57]
ma = max(number)
mi = min(number)
le = len(number)
su = sum(number)
avg = su/le
print(ma, mi, le, su, avg)
