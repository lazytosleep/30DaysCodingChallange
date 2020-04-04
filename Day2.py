def doXOR(nums) -> int:
    xors = 0
    for i in range(0, len(nums)):
        xors = xors ^ nums[i]
    return xors


print(doXOR([4, 1, 3, 2, 3, 1, 2]))