
class Solution:
    def maxChunksToSorted(self, arr) -> int:
        minOfRight = [None] * len(arr)
        minOfRight[len(arr) - 1] = arr[len(arr) - 1]
        for index in range(0, arr.__len__())[::-1]:
            if (index <= len(arr) - 2):
                minOfRight[index] = min(minOfRight[index + 1], arr[index])
        result = 0
        maxResult = 0
        for index in range(len(arr)-1):
            maxResult = max(maxResult, arr[index])
            if (maxResult <= minOfRight[index+1]):
                result = result + 1
        return result + 1

t = Solution()
result = t.maxChunksToSorted([0,0,1,1,1])
print(result,'5')

print(t.maxChunksToSorted([2,1,3,4,4]),'4')

print(t.maxChunksToSorted([5,4,3,2,1]),'1')































