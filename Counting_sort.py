def CountingSort(lst):
	left=min(lst)
	right=max(lst)
	Range=right-left+1
	count=[0 for x in range(Range)]
	sortedArray=lst[:]
	for i in range(0,len(lst)):
		count[lst[i]-left]+=1
	for i in range(1,Range):
		count[i]+=count[i-1]
	for i in range(0,len(lst)):
		count[lst[i]-left]-=1
		sortedArray[count[lst[i]-left]]=lst[i]
	print("Sorted array:",sortedArray)
if __name__=='__main__':
	l=list(map(int,input('Enter array elements ').split(' ')))
	CountingSort(l)