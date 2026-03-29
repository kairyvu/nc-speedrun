class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        posSpeed = list(zip(position, speed))
        posSpeed.sort()

        # time = (target - position) / speed
        fleets = len(posSpeed)
        currFleetTime = -1
        for i in range(len(posSpeed) - 1, -1, -1):
            pos, sp = posSpeed[i]
            time = (target - pos) / sp
            if currFleetTime < time:
                currFleetTime = time
            else:
                fleets -= 1

        return fleets