class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        Map = Counter(nums)

        for value, freq in Map.items():
            if freq > 1:
                return True
        return False
        