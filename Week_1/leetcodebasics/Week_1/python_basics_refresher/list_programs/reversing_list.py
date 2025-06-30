def listReverse(list_id):
    rlist_id=list_id[::-1]
    return rlist_id
list_id=[]
ch=1
while ch==1:
    j=int(input("Enter elements: "))
    list_id.append(j)
    ch=int(input("Do you wish to continue?\t (press 1 to continue, 0 to stop): "))
print(listReverse(list_id))