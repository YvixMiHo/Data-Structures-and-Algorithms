# Input: nums = [1,1,2]
# Output: 2, nums = [1,2,_]
# Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).
from pandas.core.internals.construction import arrays_to_mgr

# lets discuss the algoritm.
# we want to take an array nums process it.
# it should count number of unqiue elements k, and return nums where duplicated elements have been removed.
# to do this we should take nums we want to create two pointers (indexs) that will travel the array and
# compare the elements at the array to check if they are equal
# p1 will travel the array
# p2 will only travel the array when a unique item has been found.

# LC 1929
# Given an integer array nums of length n, you want to create an array ans of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).
# Specifically, ans is the concatenation of two nums arrays.
# Return the array ans.

 # array = [a1,a2,...an]
 # desired = [a1,a2,...an, a1, a2, ... an]
 #              0  1     n   n+1 n+2     n+n
 #array = [1 , 2, 3]
 # take the length of the array
 # we will iterate length of the array
 # we will append the a[i] element on each pass through




from tests.test_helper_func import check_ascending

def removeElements(nums,key):

    k = 0
    L = len(nums)
    q = L-1
    for p in range(L):
        if nums[L-1-p] != key:
            k+=1
        else:
            #nums[L-1-p]='_'
            nums[L - 1 - p] , nums[q]  = nums[q], nums[L - 1 - p]
            q -= 1
    return k

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

def selfConcatenation(array):
    ans = array
    if not ans:
        return ans
    else:
        return ans+ans