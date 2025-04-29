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


        # answer=[]
        # preffix=1
        # for i in range(len(nums)):
        #     if i==0:
        #         preffix=1
        #     else:
        #         preffix=preffix*nums[i-1]
        #     suffix=prod(nums[i+1:len(nums)+1])
        #     answer.append(preffix*suffix)
        # return answer
        

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