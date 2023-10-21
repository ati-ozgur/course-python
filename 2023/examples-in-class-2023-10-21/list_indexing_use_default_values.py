list1 = ["zero","one","two","three","four","five"]

# we can use range like structure to index the list
# instead of one element, we get sublist
# start:end:step
# if I do not give start, it is assumed 0
# if I do not give end, it is assument length of list (or end of list)
sublist1 = list1[:3]
print(sublist1)

sublist2 = list1[3:]
print(sublist2)


sublist3 = list1[::-1]
print(sublist3)
