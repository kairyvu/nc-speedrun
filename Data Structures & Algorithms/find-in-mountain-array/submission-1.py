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

        def findTarget(l, r, slope):
            while l <= r:
                mid = (l + r) // 2
                midVal = mountainArr.get(mid)
                if midVal == target:
                    return mid
                elif slope * target < slope * midVal:
                    r = mid - 1
                else:
                    l = mid + 1
            return -1

        leftPart = findTarget(0, mountainTop, 1)
        return leftPart if leftPart != -1 else findTarget(mountainTop + 1, length, -1)