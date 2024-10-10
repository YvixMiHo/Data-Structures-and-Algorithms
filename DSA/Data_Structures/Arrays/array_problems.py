# Input: nums = [1,1,2]
# Output: 2, nums = [1,2,_]
# Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).

# lets discuss the algoritm.
# we want to take an array nums process it.
# it should count number of unqiue elements k, and return nums where duplicated elements have been removed.
# to do this we should take nums we want to create two pointers (indexs) that will travel the array and
# compare the elements at the array to check if they are equal
# p1 will travel the array
# p2 will only travel the array when a unique item has been found.
from tests.test_helper_func import check_ascending

def removeDuplicates(array):
    if not array or (False == check_ascending(array)):
        k = 0
    else:
        k = 1
        for ptr1 in range(1,len(array)):
            if array[ptr1] != array[ptr1-1]:
                k+=1
                array[k-1] = array[ptr1]
        for i in range(k,len(array)):
                array[i] = '_'
    return k