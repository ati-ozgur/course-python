

start =12
end = 20

#12,13,14,15,16,17,18,19

print(list(range(start,end)))

start =12
end = 20
step = 3
# 12, 15,18
print("an example with start end step")
print(list(range(start,end,step)))


start =12
end = 10

# empty
print("empty")
print(list(range(start,end)))


start =12
end = 10
step= -1
# 12,11
print("an example with start end, negative step")
print(list(range(start,end,step)))
