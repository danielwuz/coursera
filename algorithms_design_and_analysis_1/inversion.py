def inversion(nums):
    if len(nums) <= 1:
        return nums, 0
    m = len(nums) // 2
    left, l = inversion(nums[:m])
    right, r = inversion(nums[m:])
    merged, m = merge(left, right)
    return merged, l + r + m


def merge(left, right):
    i, j = 0, 0
    count = 0
    merged = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
            count += (len(left) - i)
    if i < len(left):
        merged.extend(left[i:])
    if j < len(right):
        merged.extend(right[j:])
    return merged, count


def main():
    with open('./data/IntegerArray.txt') as f:
        num = [int(a) for a in f.readlines()]
    print inversion(num)[1]


main()
