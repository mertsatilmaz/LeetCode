class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums)<=1:
            return print("List must have an index")
            
        dict_first = {}
        for i in range(len(nums)):
            if nums[i] in dict_first:
                return [dict_first[nums[i]],i]
            else:
                dict_first[target-nums[i]]=i
                
                