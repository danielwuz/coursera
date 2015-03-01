def selection_sort(nums):
    for i in range(len(nums)):
        k = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[k]:
                k = j
        nums[i], nums[k] = nums[k], nums[i]
    return nums


def insertion_sort(nums):
    for i in range(len(nums)):
        for k in range(i, 0, -1):
            if nums[k] < nums[k - 1]:
                nums[k], nums[k - 1] = nums[k - 1], nums[k]
            else:
                break
    return nums


def h_sort(nums, h):
    for i in range(len(nums)):
        for k in range(i, 0, -h):
            if nums[k] < nums[k - h]:
                nums[k], nums[k - h] = nums[k - h], nums[k]
            else:
                break
    return nums


def shellsort(nums):
    # determin range
    x = 0
    while 3 * x + 1 < len(nums):
        x += 1
    # shellsort
    while x >= 0:
        h_sort(nums, 3 * x + 1)
        x -= 1
    return nums


from random import randint


def shuffle(nums):
    for i in range(len(nums)):
        k = randint(0, i)
        nums[k], nums[i] = nums[i], nums[k]
    return nums


test = [randint(1, 100) for _ in range(100)]
