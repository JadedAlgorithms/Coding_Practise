'''
Basically I sort a list w/o using sort function. 
I plan to use bubble sort but i already know that.
Maybe I should try learning a new algorithm?
'''
def mergeSort(list_id):
    #recursive case
    if len(list_id)<=1:
        return list_id
    else: 
        mid=len(list_id)//2
        left=mergeSort(list_id[:mid])
        right=mergeSort(list_id[mid:])
    return merge(left,right)
def merge(left,right):
    sortedList=[]
    i=j=0
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            sortedList.append(left[i])
            i+=1
        else: 
            sortedList.append(right[j])
            j+=1
    sortedList.extend(left[i:])
    sortedList.extend(right[j:])
    return sortedList
list1=[12,32,1,30,17,19,3,7,14]
print(mergeSort(list1))
