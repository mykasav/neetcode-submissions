class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
   
        hash_map={}
        for i,numa in enumerate(nums):
            hash_map[numa]=i
        
        for i,numa in enumerate(nums):
            compl=target-numa
            if compl in hash_map and hash_map[compl]!=i:
                return [i,hash_map[compl]]
        return []