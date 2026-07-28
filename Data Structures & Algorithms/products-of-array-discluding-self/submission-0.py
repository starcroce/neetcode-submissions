class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_product_list = [1 for _ in range(len(nums))]
        suffix_product_list = [1 for _ in range(len(nums))]

        curr = 1
        for i in range(1, len(nums)):
            curr *= nums[i-1]
            prefix_product_list[i] = curr

        curr = 1
        for i in range(len(nums)-2, -1, -1):
            curr *= nums[i+1]
            suffix_product_list[i] = curr

        res = [
           prefix_product_list[i] * suffix_product_list[i]
           for i in range(len(nums))
        ]
        return res