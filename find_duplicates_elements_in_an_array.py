#Given an array of integers, find if the array contains any duplicates.
#Your function should return true if any value appears at least twice in the array, 
# and it should return false if every element is distinct.
#Example 1:
#Input: [1,2,3,1]
#Output: true
#Example 2:
#Input: [1,2,3,4]
#Output: false

# BRUTE FORCE METHOD, TIME COMPLEXITY - O(n^2) since nested for loops are present
# we just need to traverse the elements and find a pair that match
# Consider a index and search all the index after that to find a matching number

my_array = [1,8,4,6,3,5,11,9]
my_array1 = [1,8,4,6,3,11,11,9]
my_array2 = [1,2,3,4,5,6,7,9]

def findDuplicateElemts(my_array):
    for ch1 in range(0,len(my_array)):
        for ch2 in range(ch1+1,len(my_array)):
            if(my_array[ch1]==my_array[ch2]):
                print(f"The values of ch1 and ch2 are {my_array[ch1]} and {my_array[ch2]}")
                return True
    return False

print(findDuplicateElemts(my_array))

#BETTER APPROACH - sort the array and traverse through the array only once
#TIME COMPLEXITY - O(nlogn)

def findDuplicateWithSort(my_array1):
    my_array1.sort()
    print(my_array1)
    for ch in range(0,len(my_array1)-1):
        if(my_array1[ch]==my_array1[ch+1]):
            return True
    return False

print(findDuplicateWithSort(my_array1))

#BEST APPROACH - USING PYTHON DICTIONARY, COMPLEXITY - O(n)

def findDuplicateWithDict(my_array2):
    dictionary = dict()
    if(len(my_array2)<2):
        return False
    else:
        for i in range(len(my_array2)):
            if my_array2[i] in dictionary:
                return True
            else:
                dictionary[my_array2[i]] = True
        return False
        

print(findDuplicateWithDict(my_array2))

