# Input: nums = [1,1,2]
# Output: 2, nums = [1,2,_]
# Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).
from ftplib import parse150

# lets discuss the algoritm.
# we want to take an array nums process it.
# it should count number of unqiue elements k, and return nums where duplicated elements have been removed.
# to do this we should take nums we want to create two pointers (indexs) that will travel the array and
# compare the elements at the array to check if they are equal
# p1 will travel the array
# p2 will only travel the array when a unique item has been found.

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

    k = removeDuplicates(nums)
    k2 = removeDuplicates(nums2)
    k3 = removeDuplicates(nums3)
    k4 = removeDuplicates(nums4)
    k5 = removeDuplicates(nums5)
    k6 = removeDuplicates(nums6)

    test_removeDuplicates(nums,expectedNums,k)
    test_removeDuplicates(nums2, expectedNums2,k2)
    test_removeDuplicates(nums3,expectedNums3,k3)
    test_removeDuplicates(nums4, expectedNums4,k4)
    test_removeDuplicates(nums5,expectedNums5,k5)
    test_removeDuplicates(nums6, expectedNums6,k6)

def main():
    test_cases()



if __name__ == "__main__":
    main()
