# Problem: Flipping an Image - https://leetcode.com/problems/flipping-an-image/description/

class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        n = len(image)
        
        for row in range(n):
           
            image[row] = [1 - bit for bit in image[row][::-1]]
        
        return image