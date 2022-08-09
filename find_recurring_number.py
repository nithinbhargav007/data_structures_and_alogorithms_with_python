#given an array of elements. Find the first recurring number

array = [1,8,9,3,9,5,5,6]

def findRecurringNum(array):
        dictionary=dict();
        if(len(array)<2):
            return None;
        else:
            for i in range(len(array)):
                if array[i] in dictionary:
                    print(f"the first recurring number is {array[i]}")
                    return True
                else:
                    dictionary[array[i]] = True
            return None

print(findRecurringNum(array))