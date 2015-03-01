from random import randint


def quick_sort(nums):
    _quick_sort(nums, 0, len(nums) - 1)


def _quick_sort(nums, start, end):
    if start >= end:
        return
    i = _partition(nums, start, end)
    _quick_sort(nums, start, i - 1)
    _quick_sort(nums, i + 1, end)


def _partition(nums, start, end):
    # random shuffling
    r = randint(start, end)
    nums[start], nums[r] = nums[r], nums[start]
    pivot = nums[start]
    i = start + 1
    for j in range(start + 1, end + 1):
        if nums[j] >= pivot:
            continue
        nums[i], nums[j] = nums[j], nums[i]
        i += 1
    nums[start], nums[i - 1] = nums[i - 1], nums[start]
    return i - 1


test = [randint(0, 100) for _ in range(1000)]
# quick_sort(test)
import timeit
timer = timeit.Timer("quick_sort(test)", "from quick_sort import quick_sort; from quick_sort import test;")
# print timer.timeit(1)


def quick_select(nums, k):
    '''k is 0 based'''
    low, high = 0, len(nums) - 1
    while low <= high:
        i = _partition(nums, low, high)
        if i == k:
            return nums[k]
        elif i > k:
            high = i - 1
        else:
            low = i + 1
    raise ValueError("Cannot reach here")


def quick_select_all(nums, k):
    '''k is 0 based'''
    low, high = 0, len(nums) - 1
    while low <= high:
        i = _partition(nums, low, high)
        if i == k:
            return nums[:k]
        elif i > k:
            high = i - 1
        else:
            low = i + 1
    raise ValueError("Cannot reach here")


test = [randint(0, 10) for _ in range(10)]
print test
print quick_select_all(test, 5)


# TODO: very important!
def _partition_three_way(nums, start, end):
    pivot = nums[start]
    lo, hi = start + 1, end
    i = start + 1
    while i < hi:
        if nums[i] == pivot:
            i += 1
        elif nums[i] < pivot:
            nums[lo], nums[i] = nums[i], nums[lo]
            lo += 1
            i += 1
        else:  # >
            nums[hi], nums[i] = nums[i], nums[hi]
            hi -= 1
    nums[start], nums[lo - 1] = nums[lo - 1], nums[start]
    return lo - 1, hi
