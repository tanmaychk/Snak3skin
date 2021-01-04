name = input("Enter file name: ")
fhand = open(name)

count = 0
for line in fhand:
    if line.startswith("X-DSPAM-Confidence:") : 
        count = count + 1

total = 0
for line in fhand:
    if line.startswith("X-DSPAM-Confidence:"):
       line = float(line[21:])
       total = line + total
       
average = total/ count

print("Average spam confidence:",average)

