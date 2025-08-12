#empty list
my_list = []

#elements append(10,20,30,40)
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

#insert 15 to 2nd position(index start from 0,1,2,.......)
my_list.insert(1, 15)

#extend with [50,60,70]
my_list.extend([50, 60, 70])

#remove last element
#for first element  .pop(0)
my_list.pop()

#sort in ascending
#for descending  .sort(reverse=True)
my_list.sort()

#find index of value 30 and then print index of 30
index_30 = my_list.index(30)
print("The index of 30: ", index_30)