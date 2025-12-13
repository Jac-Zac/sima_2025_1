def robust_sum(numbers: list) -> int:
    total = 0
    for n in numbers:
        if isinstance(n, int) or isinstance(n, float):
            total = total + n
        else:
            continue
    return total