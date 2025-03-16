# Problem: Pancake Sorting - https://leetcode.com/problems/pancake-sorting/

class Solution(object):
    def pancakeSort(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        ans = []
        last = len(arr)
        for i in range(len(arr)-1, 0, -1):
            j = arr.index(max(arr[:i+1]))
            ans.append(j+1)
            arr = arr[j::-1] + arr[j+1:]
            ans.append(last)
            last -= 1
            arr = arr[last::-1] + arr[last+1:]

        return ans
                