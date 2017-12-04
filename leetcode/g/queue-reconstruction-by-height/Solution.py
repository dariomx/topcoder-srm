from collections import deque


class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        people = deque(sorted(people, key=lambda (a, b): (b, a)))
        queue = []
        tmp = deque()
        while people:
            (h, k) = people.popleft()
            if h == 0:
                queue.append((h, k))
            else:
                cnt = 0
                for (h1, _) in queue:
                    if h1 >= h:
                        cnt += 1
                if cnt == k:
                    queue.append((h, k))
                    people.extendleft(tmp)
                    tmp.clear()
                else:
                    tmp.append((h, k))
        while tmp:
            queue.append(tmp.popleft())
        return queue
