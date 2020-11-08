name = input("whats your name? ")
fnd = name.find("user")
if fnd == 0:
    print("choose another name")
else:
    print("hello",name)
