# Problem: fruit-into-baskets - https://leetcode.com/problems/fruit-into-baskets/

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        start = 0
        max_fruits = 0
        fruit_count = {}
        
        for end, fruit in enumerate(fruits):
            fruit_count[fruit] = fruit_count.get(fruit, 0) + 1
            
            while len(fruit_count) > 2:
                fruit_count[fruits[start]] -= 1
                if fruit_count[fruits[start]] == 0:
                    del fruit_count[fruits[start]]
                start += 1
            
            max_fruits = max(max_fruits, end - start + 1)
        
        return max_fruits 