"""
I kind of recall a similar problem from interviewcake.com, or similar. So this is not entirely my creation; but I fetched the pieces from my rotten memory.

The trick is to keep an stack of indices, where the top is always the closest index of the warmer temperature; at least among the so-far-seen ones (we will process the array backwards).

At day i-th, if the temperature at i+1 is bigger; we are lucky and the wait time for warmer weather is simply 1. But if the next temperature is less or equal, then we pop from stack until we find something greater. The order in which indices were added to such stack, guarantees that we pick the closest one. If we find such element then we compute days difference (index difference), and keep the entry (in order to maintain the stack invariant). Finally, regardless of which case we fell into, we add also the temperature index to stack (because earlier temperatures may need this one).

The biggest confusion when I saw this solution was: why can I simply remove indices from the stack, until I find one that corresponds bigger than current temperature? The reason is that temperature i-th will get added to stack anyway, and per order of processing, any earlier temperature that is smaller will pick first temperature i-th; the removed elements are not really needed (there is someone bigger that appears first). And what if we find bigger temperatures earlier in time? Well, those guys will not care either about the removed entries (cause condition is to find something warmer).

It is such pruning of the stack that makes this algorithm efficient. Actually, if I remember correctly is linear. This is because every element is added/removed at most once from the stack, thus the accumulated extra cost of the nested loop will be O(n); adding to the cost of main iteration will keep it as O(n).

"""

class Solution(object):
    def dailyTemperatures(self, temperatures):
        n = len(temperatures)
        wait = [0] * n
        closest_gt = [n-1]
        for i in xrange(n-2, -1, -1):
            if temperatures[i+1] > temperatures[i]:
                wait[i] = 1
            else:
                while closest_gt:
                    j = closest_gt[-1]
                    if temperatures[j] > temperatures[i]:
                        wait[i] = j - i
                        break
                    else:
                        closest_gt.pop()
            closest_gt.append(i)
        return wait
