# Declare variables
mylist = [2,3,1,3,5,3,3,3,3]   # Our inputs to the program
has_duplicates = False # initialize as false (why?)

# TODO: Sort 'myList' (Why do we sort first?)
mylist.sort()
# TODO: Loop through 'mylist' with a for-Loop
print()
for index in range(len(mylist) - 1):
    print(index)
    print(mylist[index], mylist[index + 1])
    # TODO: Check if adjacent elements of 'mylist' are the same
    if mylist[index] == mylist[index + 1] :
        # TODO: if they are the same, set has_duplicates to True
        has_duplicates = True
        print()
        print("{} is duplicated".format(mylist[index]))
        break


a = 1
for mylist[index] in mylist :
    if mylist[index] == True :
        a += 1
        print("{} time(s)".format(a))
        # TODO: Exit out of the for-loop (no need to check rest of list)

print(has_duplicates) # Our outputs of the program
