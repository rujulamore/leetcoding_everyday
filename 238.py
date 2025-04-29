class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        import math
        # ans=[]
        # for i in range(len(nums)):
        #     prod=1
        #     for j in range(len(nums)):
        #         if j!=i:
        #             prod=prod*nums[j]
        #     ans.append(prod)
        
        # return ans
        #print(nums[3:4])


        
        

        output=[]
        l=len(nums)-1
        prefix=1
        for num in nums:
            output.append(prefix)
            prefix *= num       
        right=1
        while l>=0:
            output[l]=output[l]*right
            right=right*nums[l]
            l=l-1
        return output
