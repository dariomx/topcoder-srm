from collections import Counter
from sys import maxsize as maxint


class Solution:
    def leastInterval(self, tasks, n):
        cache = dict()
        def rec(task_cnt, task_sched, clock, seq):
            print(cache)
            print(seq)
            if not task_cnt:
                return 0
            else:
                if seq in cache:
                    return cache[seq]
                min_idle = maxint
                for task, sched in list(task_sched.items()):
                    if sched <= clock:
                        task_cnt[task] -= 1
                        if task_cnt[task] == 0:
                            del task_cnt[task]
                            del task_sched[task]
                        else:
                            task_sched[task] = clock + n + 1
                        idle = rec(task_cnt, task_sched, clock + 1, seq+task)
                        cache[seq+task] = idle
                        min_idle = min(min_idle, idle)
                        if task not in task_cnt:
                            task_cnt[task] = 0
                        task_cnt[task] += 1
                        task_sched[task] = sched
                if min_idle == maxint:
                    min_idle = 1 + rec(task_cnt, task_sched, clock + 1, seq)
                cache[seq] = min_idle
                return cache[seq]

        task_cnt = Counter(tasks)
        task_sched = dict([(task, 0) for task in task_cnt.keys()])
        return len(tasks) + rec(task_cnt, task_sched, 0, "")


tasks = ["A","A","A","B","B","B"]
#tasks = ["B"]
n = 10
print(Solution().leastInterval(tasks, n))