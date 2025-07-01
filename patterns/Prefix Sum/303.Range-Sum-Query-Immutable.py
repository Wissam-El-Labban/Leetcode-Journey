class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix = []
        cur = 0
        for n in nums:
            cur += n
            self.prefix.append(cur)
    def sumRange(self, left: int, right: int) -> int:
        rightSum = self.prefix[right]
        leftSum = self.prefix[left - 1] if left > 0 else 0
        return (rightSum -leftSum)


#original solution by: Neetcode
#video link: https://www.youtube.com/watch?v=2pndAmo_sMA

#we created a prefix as can be shown which takes the complete sum of every array element with everythin that came before it.
#we need to exclude the sum of the elements before the left index hence why we subtract it by 1 or initialize it to 0 if it is the first most index just as defined in the prefix sum method.


