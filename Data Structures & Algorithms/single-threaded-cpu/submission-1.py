class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        taskList = []
        earliest = float("inf")
        for index, task in enumerate(tasks):
            taskList.append((task[0], task[1], index))
            earliest = min(earliest, task[0])
        
        taskList.sort()
        minHeap = []
        index = 0
        for et, pt, i in taskList:
            if earliest != et:
                break
            heapq.heappush(minHeap, (pt, i))
            index += 1
        
        res = []
        time = earliest
        while minHeap or index < len(taskList):
            if minHeap:
                pt, i = heapq.heappop(minHeap)
                res.append(i)
                time += pt
                while index < len(taskList) and time >= taskList[index][0]:
                    heapq.heappush(minHeap, (taskList[index][1], taskList[index][2]))
                    index += 1
            else:
                startTime = taskList[index][0]
                while startTime == taskList[index][0]:
                    heapq.heappush(minHeap, (taskList[index][1], taskList[index][2]))
                    index += 1
        return res