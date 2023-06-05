"""
This approach is an optimized version of the first acceptance. It uses only one list to store the products.
"""
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        result = []

        #filling the prefix list
        result.append(product) #making the prefix of the first number 1 by default

        for index in range(0, len(nums)-1, 1):
            product *= nums[index]
            result.append(product)
        print(result)
        
        #filling the postfix list
        product = 1
        for index in range(len(nums)-1, 0, -1):
            product *= nums[index]
            result[index-1] *= product 

        return result
        