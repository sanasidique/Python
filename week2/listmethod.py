

list1 = input("Enter the first list of integers separated by spaces: ").split()
list2 = input("Enter the second list of integers separated by spaces: ").split()
for i in range(len(list1)):
    list1[i] = int(list1[i])
for i in range(len(list2)):
    list2[i] = int(list2[i])
if len(list1) == len(list2):
    print("The lists are of the same length.")
else:
    print("The lists are of different lengths.")
if sum(list1) == sum(list2):
    print("The lists sum to the same value.")
else:
    print("The lists sum to different values.")
common_values = set(list1) & set(list2) 
if common_values:
    print("Common values:", common_values)
else:
    print("No common values.")
