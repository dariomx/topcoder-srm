"""
Simple Python3 recursive solution, O(2^n) time complexity

There is a nice pattern when going from n-1 to n. Let us begin with n = 1,
where the only option is:

0
1

Now, let us leverage this sequence for n = 2. One way of doing that,
is to first generate the first half of the new sequence by prefixing with
zero the n-1 sequence:

00
01

And for the second half, we suspect that the prefix will be one; but what
about the rest? we can not just put:

00
01
10
11

Cause between snd and trd elements there is more than one bit of difference.
But we notice that if we reverse the n-1 sequence, the constraints are met:

00
01
11
10

Let us repeat the exercise for n = 3, first duplicate the n-1 sequence: first
occurrence (half) in same order and second one reversed.

00
01
11
10
10
11
01
00

Now we just prefix first and second halves with zero and one respectively:

000
001
011
010
110
111
101
100

Same thing occurs for n = 4:

0000
0001
0011
0010
0110
0111
0101
0100
1100
1101
1111
1110
1010
1011
1001
1000

Why this works? Is sort of divide and conquer strategy: once we have the n-1
sequence, and we know that its reverse its also another gray code for n-1.
Putting a constant prefix to either sequence will not alter its "gray-codeness"
nature, as that prefix will remain constant (the other n-1 bits are the ones
changing).

The only trick is the transition between the two halves, where we repeat the
same element. That gets solved by the difference in prefixes, as that is the
only moment where that first bit changes.

Time complexity is given by recursive definition:

T(0) = 1
T(1) = 2
T(n) = 2 * T(n-1)

The last equation is a "linear first order homogeneous difference equation" of
the form:

a*T(n) + b*T(n-1) = 0

whose general solution is given by:

T(n) = C*(-b/a)^n

where C is determined by initial conditions. Applying to our example
with a=1 and b=-2, leads us to the generic solution of:

T(n) = C * 2^n

We could apply one of the base cases of recursion as initial condition, eg

T(1) = 2

and substitute to find the C:

2 = C * 2^1 = 2 * C   ==>   C = 1

same result should lead with the other initial condition:

T(0) = 1 = C * 2^0 = C    ==>   C = 1

Therefore our complexity function is just

T(n) = 2^n

which is clearly O(2^n)

Note: we could have concluded that since we got the form T(n) = C * 2^n, but
is always nice to review this type of material (I kinda forgot it).

"""

class Solution(object):
    def grayCode(self, n):
        if n <= 0:
            return [0]
        elif n == 1:
            return [0, 1]
        else:
            half0 = self.grayCode(n - 1)
            half1 = [(1 << (n - 1)) | x for x in reversed(half0)]
            return half0 + half1
