def selection_sort(nums):
    nums_size = len(nums)
    for i in range(nums_size):
        smallest_index = i
        for j in range(smallest_index+1, nums_size):
            if nums[j] < nums[smallest_index]:
                smallest_index = j
        nums[i], nums[smallest_index] = nums[smallest_index], nums[i]        
            
    return nums    


# don't touch below this line


def test(nums):
    result = selection_sort(nums.copy())
    print(f"Original list: {nums}")
    print(f"List after custom sort: {result}")
    print("====================================")


def main():
    test([5, 3, 8, 6, 1, 9])
    test([10, 5, 3, 7, 2, 8, 1])
    test([15, 12, 8, 7, 5, 3, 1])
    test([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    test([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])


main()
