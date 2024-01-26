def find_common_elements(list1, list2, list3):
    commonElements = set()
    for i in list1:
        if i in list2 and i in list3:
            commonElements.add(i)
    return commonElements
 
list1 = [1, 2, 10, 20, 30, 80]
list2 = [5, 6, 20, 80, 10]
list3 = [3, 4, 15, 20, 30, 70, 80, 10]
 
commonElements = find_common_elements(list1, list2, list3)

print(commonElements)