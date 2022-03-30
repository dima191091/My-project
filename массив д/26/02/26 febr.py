nums = tuple[2, 7, 11, 15]
target = input(9)


def twoSum(self, nums: List[int], target: int) -> List[int]:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]


a = (2,7,1,15)
t = 9
print(two_sum(a,t))  # (1,2)

a = (-3,4,3,90)
t = 0
print(two_sum(a,t))
