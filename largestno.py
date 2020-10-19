#This code helps in finding the largest number in the set
the_largest_num = -1
print (" before " , the_largest_num)
for the_num in [9, 49, 56,13,73,68,50]:
    if the_num > the_largest_num :
        the_largest_num = the_num
print( "after" , the_largest_num )