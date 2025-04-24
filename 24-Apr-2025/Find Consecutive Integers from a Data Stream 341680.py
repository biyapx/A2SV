# Problem: Find Consecutive Integers from a Data Stream - https://leetcode.com/problems/find-consecutive-integers-from-a-data-stream/

from collections import deque 

class DataStream:

    def __init__(self, value: int, k: int):
        self.stream = deque()
        self.k = k
        self.value = value
        self.count = 0
    def consec(self, num: int) -> bool:
        self.stream.append(num)

        if num == self.value:
            self.count = min(self.count +1, self.k)
        else:
            self.count = 0
        if len(self.stream) == self.k:
            self.stream.popleft()
        return self.count == self.k
        


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)