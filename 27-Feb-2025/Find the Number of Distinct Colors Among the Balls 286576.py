# Problem: Find the Number of Distinct Colors Among the Balls - https://leetcode.com/problems/find-the-number-of-distinct-colors-among-the-balls/description/

class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        ball_colors = {}
        color_counts = {}
        result = []
        
        for ball, color in queries:
            if ball in ball_colors:
                old_color = ball_colors[ball]
                color_counts[old_color] -= 1
                
                if color_counts[old_color] == 0:
                    del color_counts[old_color]
            
            ball_colors[ball] = color
            color_counts[color] = color_counts.get(color, 0) + 1
            result.append(len(color_counts))
        
        return result