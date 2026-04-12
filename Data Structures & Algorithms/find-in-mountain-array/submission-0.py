class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        length = mountainArr.length()
        l, r = 0, length - 1
        while l < r:
            mid = (l + r) // 2
            midVal = mountainArr.get(mid)
            nextVal = mountainArr.get(mid + 1)

            if midVal < nextVal:
                l = mid + 1
            else:
                r = mid

        mountainTop = l

        l, r = 0, mountainTop
        while l <= r:
            mid = (l + r) // 2
            midVal = mountainArr.get(mid)
            if midVal == target:
                return mid
            elif target < midVal:
                r = mid - 1
            else:
                l = mid + 1

        l, r = mountainTop, length - 1
        while l <= r:
            mid = (l + r) // 2
            midVal = mountainArr.get(mid)
            if midVal == target:
                return mid
            elif target < midVal:
                l = mid + 1
            else:
                r = mid - 1
        
        return -1