# lets discuss the algoritm for removing duplicates LC
# we want to take an array nums process it.
# it should count number of unqiue elements k, and return nums where duplicated elements have been removed.
# to do this we should take nums we want to create two pointers (indexs) that will travel the array and
# compare the elements at the array to check if they are equal
# p1 will travel the array
# p2 will only travel the array when a unique item has been found.
#from idlelib.configdialog import changes


#lets discuss algorithm for removing an element LC 27
#prompt given an array and integer val remove all occurences of val in nums in place
#the order of element can be changed, then retunr number of elements in nums which are not equal to val.
#nums should be changed such that first k elements of array contain number of elements which are not equalt to val.
# we go with 1 pointer approach, we want to travel the array and at each occurence see if array value at index(pointer) is equal
# to key(val), if array at index is not equal to the key, continue moving pointer forward,
# if it is set the array at that pointer to '_'.

# key = 2  -> 1  3  _ _ , k = 2
#
# 1   2   2   3  decrement p nums[p] != 2
#             p
#             q
#
# 1   2   2   3   nums[p] == 2 replace with _, then we swap value with whats at nums[q] we also want to decrement q
#         p
#             q
#
# 1   2   3   _   nums[p] == 2 replace with _, then we swap value with whats at nums[q]
#     p   q
#
# 1   3   _   _   nums[p] == 2 replace with _, then we swap value with whats at nums[q]
# p   q

def removeElements(nums,key):

    k = 0
    L = len(nums)
    q = L-1
    for p in range(L):
        if nums[L-1-p] != key:
            k+=1
        else:
            nums[L-1-p]='_'
            nums[L - 1 - p] , nums[q]  = nums[q], nums[L - 1 - p]
            q -= 1
    return k

nums = [1, 2, 2]
nums2 = [0,0,1,1,1,2,2,3,3,4]
nums3 = [-2,-1,-1,0,1,2,2]
nums4 = [-4,-3,-3,-2,-2,-1,-1,0,0]
nums5 = [0]
nums6 = []

expectedNums = [1,2,'_']
expectedNums2 = [0, 1, 2, 3, 4, '_', '_', '_', '_', '_']
expectedNums3 = [-2,-1,0,1,2, '_','_']
expectedNums4 = [-4,-3,-2,-1,0,'_', '_', '_', '_', '_']
expectedNums5 = [0]
expectedNums6 = []

def removeDuplicates(array):
    if len(array) == 0:
        k = 0
    elif len(array) == 1:
        k = 1
    else:
        k = 1
        for ptr1 in range(1,len(array)):
            if array[ptr1] != array[ptr1-1]:
                k+=1
                array[k-1] = array[ptr1]
        for i in range(k,len(array)):
                array[i] = '_'
    print(array)
    print(k)
    return k





def test_removeDuplicates(array1, array2, length):
    #assert len(array1) == length, f"array does not have same length as k, {len(array1)}, {length}"
    for i in range(length):
        assert array2[i] == array1[i], f"values in array do not match: {array1[i]}, {array2[i]}"

def test_cases():
    global expectedNums
    global expectedNums2
    global expectedNums3
    global expectedNums4
    global expectedNums5
    global expectedNums6

    global nums
    global nums2
    global nums3
    global nums4
    global nums5
    global nums6

    new_nums=nums

    # k = removeDuplicates(nums)
    # k2 = removeDuplicates(nums2)
    # k3 = removeDuplicates(nums3)
    # k4 = removeDuplicates(nums4)
    # k5 = removeDuplicates(nums5)
    # k6 = removeDuplicates(nums6)
    #
    # test_removeDuplicates(nums,expectedNums,k)
    # test_removeDuplicates(nums2, expectedNums2,k2)
    # test_removeDuplicates(nums3,expectedNums3,k3)
    # test_removeDuplicates(nums4, expectedNums4,k4)
    # test_removeDuplicates(nums5,expectedNums5,k5)
    # test_removeDuplicates(nums6, expectedNums6,k6)

    print(new_nums)
    n=removeElements(new_nums,2)
    print(new_nums)
    print(n)

def main():
    test_cases()



if __name__ == "__main__":
    main()
