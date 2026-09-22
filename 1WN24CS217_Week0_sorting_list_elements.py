my_list=[]
num=int(input("Enter a number:"))

for i in range(0,num):
  my_list.append(int(input("enter item: ")))
print("before sorting: ",my_list)

def sort():
  for i in range(0,num):
    for j in range(i+1,num):
      if(my_list[i]>my_list[j]):
        temp=my_list[i]
        my_list[i]=my_list[j]
        my_list[j]=temp

sort()
print("sorted order is: ", my_list)
