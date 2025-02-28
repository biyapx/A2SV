# Problem: Frequency Tracker - https://leetcode.com/problems/frequency-tracker/description/

from collections import defaultdict

class FrequencyTracker:
    def __init__(self):
        self.num_count = defaultdict(int)
        self.freq_count = defaultdict(int) 

    def add(self, number: int) -> None:
        if self.num_count[number] > 0:
            self.freq_count[self.num_count[number]] -= 1
        self.num_count[number] += 1
        self.freq_count[self.num_count[number]] += 1

    def deleteOne(self, number: int) -> None:
        if self.num_count[number] > 0:
            self.freq_count[self.num_count[number]] -= 1
            self.num_count[number] -= 1
            if self.num_count[number] > 0:
                self.freq_count[self.num_count[number]] += 1

    def hasFrequency(self, frequency: int) -> bool:
        return self.freq_count[frequency] > 0