s = raw_input()
list = map(int, s.split())
element = raw_input("Enter the element to be found: ")
def binary_search(list, l, r, element):
	if(r >= l):
		mid = l + (r - l)/2
		if (list[mid] == element) : 
            		return mid
		elif (list[mid] > element): 
            		return binary_search(list, l, mid-1, element)
		else:
			return binary_search(list, mid+1, r, element)
	else:
        	raise Exception("Element not found")

binary_search(list, 0, len(list)-1, element)
print("The index of the given value: ", index)