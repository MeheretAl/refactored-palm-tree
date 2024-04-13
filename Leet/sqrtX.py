def sqrtX(x: int) -> int:
    if x == 0 or x == 1:
        return x

    left = 0
    right = x
    while left <= right:
        mid = (left + right) // 2
        if mid * mid < x:
            left = mid + 1
        elif mid * mid > x:
            right = mid - 1
        else:
            return mid
    return right
