import time
import random


def merge_sort(nums):
    if len(nums) < 2:
        return nums

    first_half = nums[:int(len(nums)/2)]
    second_half = nums[int(len(nums)/2):]
    first_half = merge_sort(first_half)
    second_half = merge_sort(second_half)

    return merge(first_half, second_half)


def merge(first, second):
    first_copy = first.copy()
    second_copy = second.copy()
    final = []
    i = 0
    j = 0

    while i < len(first) and j < len(second):
        if first[i] <= second[j]:
            final.append(first_copy.pop(0))
            i += 1
        else:
            final.append(second_copy.pop(0))
            j += 1
    
    if first and i < len(first):
        final += first_copy
    elif first and j < len(second):
        final += second_copy

    return final
    
        
    

# don't touch below this line


def benchmark(nums, show_nums):
    start = time.time()
    test(nums, show_nums)
    end = time.time()

    timeout = 1.00

    if (end - start) < timeout:
        print(f"test completed in less than {timeout * 1000} milliseconds!")
    else:
        print(f"test took too long ({(end - start) * 1000} milliseconds). Speed it up!")
    print("====================================")


def test(nums, show_nums):
    res = merge_sort(nums.copy())
    if show_nums:
        print(f"nums: {nums}")
        print(f"sorted: {res}")
    else:
        print(f"len nums: {len(nums)}")
        print(f"len sorted: {len(res)}")
    print("------------------------------------")


def main():
    benchmark(get_nums(10), True)
    benchmark(get_nums(100), True)
    benchmark(get_nums(1000), False)
    benchmark(get_nums(10000), False)


def get_nums(num):
    nums = []
    random.seed(1)
    for i in range(num):
        nums.append(random.randint(0, len(nums)))
    return nums


main()
