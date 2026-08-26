class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #since solution must be of linear time complexity means we cannot use nested loops, how do we bypass this??
        
        #should use two pointers , let's take advantadge of the fact that the array is sorted 

        l,r= 0 , len(numbers) - 1
        while l < r :
    
            if numbers[l] + numbers[r] > target:
                r-=1
            elif numbers[l] + numbers[r] <target:
                l+=1
            else:
                return [l+1,r+1]
            

                
            