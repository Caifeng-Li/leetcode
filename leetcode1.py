nums=[3,3]
target=6

def twoSum(self, nums: List[int], target: int) -> List[int]:
    for i in range(len(nums)):
        for j in range(len(nums))[i+1:]:
            if nums[i]+nums[j] == target:
                return [i,j]

twoSum(nums,target)

