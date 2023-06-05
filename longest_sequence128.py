"""
The Approach is to sort the list and using a two pointer technique (asjacent pointers)
increment the sequence length if the two adjacent numbers differ by 1
increment the pointers position wuthout resetting the sequence counter if the adjacent numbers are equal
increment the pointers position and reset the sequence counter otherwise
finally account for the first number that isn't always counter with this approach (if the list isn't empty)
*An empty list doesn't have any number so there isn't first number that isn't accounted for in this case  

Credit: Adelaja Qowiyyu (Myself)
"""
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        l = 0
        r = l+1
        maxLength = 0
        tempLength = 0

        nums.sort()

        print(nums)
        while r < len(nums):
            #Skipping adjacent numbers that are equal 
            if nums[r] == nums[l]:
                l += 1
                r += 1
                continue
            if nums[r] - nums[l] == 1:
                tempLength += 1
                if tempLength > maxLength:
                    maxLength = tempLength
            else:
                if tempLength > maxLength:
                    maxLength = tempLength
                tempLength = 0
            l += 1
            r += 1
        
        #Accounting for the first number which is not counted in the sequence
        if len(nums) > 0:
            maxLength += 1
        
        return maxLength

