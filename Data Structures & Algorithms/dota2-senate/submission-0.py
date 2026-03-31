class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        senate = list(senate)
        i = 0
        count = 0

        while i < len(senate):
            s = senate[i]
            if s == "R":
                if count < 0:
                    senate.append("D")
                count += 1
            elif s == "D":
                if count > 0:
                    senate.append("R")
                count -= 1
            i += 1
        
        return "Radiant" if count > 0 else "Dire"