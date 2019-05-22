"""
Python3 solution with O(n) time and O(1) space

In order to do better than O(n^2), we need to find a way to obtain the F(i+1)
value from the F(i) one, in O(1) time. It took me a couple of attempts,
but finally realized that when moving from F(0) to F(1), all the elements
of the array contribute one more time than before; except for the guy which got
the multiplication by zero. This happens in general, not just for F(0) and F(1),
but below explanation refers to that sample for clarity.

A compact way to add that new contribution of everyone is just to add sum(A),
and the contribution of the special guy (multiplied by zero) was
(n-1) * A[n-1], since it was at the end of the (theoretically rotated) array.
But the sum(A) also contains A[n-1] once so we need to substract n * A[n-1],
in order to totally eliminate the contributions of A[n-1].

Therefore, we can obtain the initial value of the rotation and the sum(A), in
a single pass (aka O(n)). After that, we iterate from n-1 to 1, and for each
of those positions we know the rule to obtain the next rotation: add sum(A)
but substract n * A[i]. Finally, we just compute the maximum rotation along the
way. The two iterations imply a total of O(n), and since we did not use
additional storage other than a few variables, space is O(1).

"""

class Solution:
    def maxRotateFunction(self, A):
        n = len(A)
        rot = 0
        suma = 0
        for i in range(n):
            rot += i * A[i]
            suma += A[i]
        max_rot = rot
        for i in range(n - 1, 0, -1):
            rot = rot + suma - n * A[i]
            max_rot = max(max_rot, rot)
        return max_rot

