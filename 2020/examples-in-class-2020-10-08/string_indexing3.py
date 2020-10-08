uni = "Jacobs University"
      				  #1111111
      #01234567890123456
# start:end:increment
print(uni[1:5])

print(uni[1:10])

print(uni[:10]) # output from start goes till 10, 10 not included

print(uni[10:]) # start from 10, goes to end

print(uni[:]) # start from zero, goes to end

print(uni[::2]) # start from zero, goes to end, increment 2

print(uni[16:10:-1])
# this outputs uni 16,15,14,13,12,11 characters 

reverse_uni = uni[::-1]
print(reverse_uni)