class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1

        nums2 = nums.copy()

        for num in nums:
            product = num * product
        
        print(f"product = {product}")

        for i in range(len(nums)):
            if nums[i] != 0: 
                nums[i] = int(product / nums[i])
            else:
                zero_prod = 1
                for l in range(len(nums)):
                    if l != i:
                        zero_prod = nums2[l] * zero_prod
                        print(f"zero_product = {zero_prod}")
                nums[i] = zero_prod
        
        return nums