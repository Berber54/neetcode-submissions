class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        res_num = None
        res = []
        if nums.count(0) >= 2:
            res = [0 for num in nums]
            return res
        elif nums.count(0) == 1:
            res = [0 for num in nums]
            for num in nums:
                if num != 0:
                    product *= num
            res[nums.index(0)] = product
            return res
        else:
            for num in nums:
                product *= num
            for num in nums:
                res.append(int(product/num))
            return res