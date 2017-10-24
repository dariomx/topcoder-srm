from collections import deque

class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        people = deque(sorted(people, key=lambda (h,k): (-h,k)))
        queue = []
        while people:
            (h, k) = people.popleft()
            queue.insert(k, (h,k))
        return queue