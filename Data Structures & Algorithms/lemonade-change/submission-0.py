class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        change = defaultdict(int)

        for b in bills:
            if b == 5:
                change[b] += 1
            elif b == 10:
                if change[5] < 1:
                    return False
                change[5] -= 1
                change[b] += 1
            else:
                if change[10] > 0 and change[5] > 0:
                    change[10] -= 1
                    change[5] -= 1
                elif change[5] >= 3:
                    change[5] -= 3
                else:
                    return False
        return True