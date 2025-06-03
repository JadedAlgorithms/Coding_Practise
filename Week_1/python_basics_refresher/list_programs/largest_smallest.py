def maxnMin(list_id):
   list_id.sort()
   n=len(list_id)
   max=list_id[n-1]
   min=list_id[0]
   return max,min
list1=[12,7,9,5,13,2,14,4,1,21]
print(maxnMin(list1))