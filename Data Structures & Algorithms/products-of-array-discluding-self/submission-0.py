class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        prod = 1
        count = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                count += 1
            else:
                prod *= nums[i]

        arr = []

        for j in nums:
            if count > 1:
                arr.append(0)
            elif count == 1:
                if j == 0:
                    arr.append(prod)
                else:
                    arr.append(0)
            else:
                arr.append(int(prod / j))

        return arr