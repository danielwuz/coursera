def quick_sort(nums):
    comparisons = _quick_sort(nums, 0, len(nums) - 1)
    print "comparisons: ", comparisons
    return nums


def _quick_sort(nums, start, end):
    if start >= end:
        return 0
    total = end - start
    i = _partition(nums, start, end)
    total += _quick_sort(nums, start, i - 1)
    total += _quick_sort(nums, i + 1, end)
    return total


def _partition(nums, start, end):
    pivot = _choose_pivot(nums, start, end)
    i = start + 1
    for j in range(start + 1, end + 1):
        if nums[j] > pivot:
            continue
        nums[j], nums[i] = nums[i], nums[j]
        i += 1
    nums[start], nums[i - 1] = nums[i - 1], nums[start]
    return i - 1


def _choose_pivot1(nums, start, end):
    # use first element as pivot
    return nums[start]


def _choose_pivot2(nums, start, end):
    # use last element as pivot
    nums[start], nums[end] = nums[end], nums[start]
    return nums[start]


def _choose_pivot3(nums, start, end):
    # use median-of-three element as pivot
    m = start + (end - start) // 2
    candidates = [(nums[start], start), (nums[end], end), (nums[m], m)]
    i = sorted(candidates)[1][1]
    nums[start], nums[i] = nums[i], nums[start]
    return nums[start]


_choose_pivot = _choose_pivot3


def main():
    with open('./data/QuickSort.txt') as f:
        nums = [int(i) for i in f.readlines()]
        quick_sort(nums)

main()
