# Problem: Insert Delete GetRandom O(1) - https://leetcode.com/problems/insert-delete-getrandom-o1/description/

import random
class RandomizedSet:
    def __init__(self):
        self.randset = set()
        self.list = []

    def insert(self, val: int) -> bool:
        if val not in self.randset:
            self.randset.add(val)
            self.list.append(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.randset:
            self.randset.remove(val)
            self.list.remove(val)
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(self.list)