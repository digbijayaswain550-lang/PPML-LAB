"""WAP to create two lists first list containing 5 integers and secondlist containing 5 strings. print both the lists one
 element from each list combined at a time."""
list1 = [10, 20, 30, 40, 50]
list2 = ["Mango", "Orange", "Apple", "Banana", "Blackberry"]
for i,j in zip(list1, list2):
    print(i, j)
