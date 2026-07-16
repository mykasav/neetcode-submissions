
import heapq
from collections import Counter

class Solution(object):
    def topKFrequent(self, nums, k):
        frequencias = Counter(nums)
        return heapq.nlargest(k, frequencias.keys(), key=frequencias.get)