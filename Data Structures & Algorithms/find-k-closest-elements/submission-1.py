class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # l, r = 0, len(arr)
        # while l < r:
        #     mid = (l + r) // 2
        #     if arr[mid] >= x:
        #         r = mid
        #     else:
        #         l = mid + 1

        p1 = 0
        for p2 in range(k, len(arr)):
            if abs(arr[p2] - x) >= abs(arr[p1] - x) and arr[p1] != arr[p2]:
                break
            p1 += 1
        
        return arr[p1:p1+k]