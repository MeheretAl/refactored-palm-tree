def searchInsert(nums: list[int], target: int) -> int:
    if target in nums:
        return nums.index(target)

    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return left