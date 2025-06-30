def maxElement(list_id):
    largest=list_id[0]
    length_list=len(list_id)
    for i in range(1,length_list):
        if largest<list_id[i]:
            largest=list_id[i]
    return largest
l=[]
ch=1
while ch==1:
    j=int(input("Enter element: "))
    l.append(j)
    ch=int(input("Do you wish to continue?\t (press 1 to continue, 0 to stop): "))
print(f"The largest element of the list is {maxElement(l)}")