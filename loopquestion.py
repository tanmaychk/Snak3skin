#this code finds the max and min vlaue according to the given values in the set
largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done" :
        break
    try:
    	n=int(num)
    
    except:
    	print("Invalid input")
    	continue
        
    if largest is None:
    	largest=n
    if n > largest:
    	largest=n
    if smallest is None:
        smallest=n
    elif n < smallest:
    	smallest =n

print("Maximum is", largest)
print("Minimum is" , smallest)