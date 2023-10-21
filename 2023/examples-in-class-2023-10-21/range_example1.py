#range_example1.py
# range(start,end,step)

start = 5
end = 10
step = 2
print("first range example with only end argument")
for x in range(end):
    print(x)

print("second range example with start and end arguments")
for x in range(start,end):
    print(x)

print("third range example with start, end and step arguments")
for x in range(start,end,step):
    print(x)


print("4th range example with start, end and step arguments")
# no output here since we are trying to go from 0 to 2 with increments of 10
for x in range(start,step,end):
    print(x)

start = 10
end = 0
step = -1

print("5th range example with start, end and step arguments")
for x in range(start,end,step):
    print(x)
