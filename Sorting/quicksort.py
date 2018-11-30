#quick sort
def QuickSort(unsorted_list,low,high):
	if low<high:
		pi = partition(unsorted_list,low,high)
		QuickSort(unsorted_list,low,pi-1)
		QuickSort(unsorted_list,pi+1,high)
	
def partition(unsorted_list,low,high):

	pivot = unsorted_list[high]
	i=low-1
	for j in range(low,high):
		if  unsorted_list[j] <pivot:
			#swap i and j
			i+=1
			temp = unsorted_list[i]
			unsorted_list[i]=unsorted_list[j]
			unsorted_list[j]=temp
			
	temp = unsorted_list[i+1]
	unsorted_list[i+1]=unsorted_list[high]
	unsorted_list[high]=temp
	print (i+1,unsorted_list)
	return i+1
unsorted_list = [10, 80, 30, 90, 40, 50, 70]
print (QuickSort(unsorted_list,0,len(unsorted_list)-1))
