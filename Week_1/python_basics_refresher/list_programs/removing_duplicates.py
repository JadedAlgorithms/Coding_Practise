def removeDupli(list_id):
    unique_list=[]
    for i in list_id:
        if i not in unique_list:
            unique_list.append(i)
        else:
            continue
    list_id=unique_list
    return list_id
l=["apple",1,3,1,2,2,"apple",(1,2,3),4,1,2,3]
print(removeDupli(l))
