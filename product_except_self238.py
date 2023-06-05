"""
The approach is to create two lists one which holds the product of numbers before every number in the list
another which holds the product of numbers after every number in the list
then multiply the corresponding pre-product and post-product to get the product of the array except the value 
of each index

Approach Credit: Neetcode.io Solution
"""
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        prefix = [1]
        postfix = [1]

        #filling the prefix list
        for num in nums:
            product *= num
            prefix.append(product)
        
        #filling the postfix list
        product = 1
        for index in range(len(nums)-1, -1, -1):
            product *= nums[index]
            postfix.insert(0, product)
        
        result = []
        #generate the product of array except self list
        for i in range(len(prefix)-1):
            result.append(prefix[i]*postfix[i+1])
        
        return result